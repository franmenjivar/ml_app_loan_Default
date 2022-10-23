from django.shortcuts import render
from django.views import View
from pytz import timezone
from .models import *
import pandas as pd
import pickle
import numpy as np
from .functions import *
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import *
from django.utils.timezone import now
import warnings
from warnings import simplefilter
import uuid

'''
Views Class containing all the views that the applications uses. Two meain subclasses are being declared,ETL Data and DefaultScore.
@Author Erick
'''


# Create your views here.
'''
ETL DATA Class inheriting django View class.
This class genereates a get function/ request  that runs a ETL
Extending View class.
'''
class ETLData(View):    
    '''
    get function according two the django view classes declaration, this function will be call whenever the class is 
    instanciated.

    Two parameteres have two being passed the string proccessing_option containing the behaviour of the desire task, and
    the string client_id_url containg the client uuid.

    @Params processing_option, client_id_url
    '''
    def get(self, request,processing_option,client_id_url, *args,**kwargs):

        '''
        fnc function to catch the warnings and to  avoid be printed on the log.
        '''
        def fxn():
            warnings.warn("deprecated", DeprecationWarning)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fxn()
        simplefilter(action='ignore', category=FutureWarning)

        
        
        # machine learning model being imported and being initialized
        svm = pickle.load(open("classifier/clf_svcFriday.sav",'rb'))

        #modelToUse is a variable containing the model to be used in the algorithm, in the case that more than one ml model is called.
        modelToUse = svm

        #Columns to be called from the dataset
        columnasDeDF3 = ['Cliente_id','numeroCuotasM5','numeroCuotasM4','numeroCuotasM3','numeroCuotasM2','numeroCuotasM1','CuotaspagadasAtiempoM5','CuotaspagadasAtiempoM4',
                        'CuotaspagadasAtiempoM3','CuotaspagadasAtiempoM2','CuotaspagadasAtiempoM1','PorcentajePagoATiempoM5','PorcentajePagoATiempoM4','PorcentajePagoATiempoM3',
                        'PorcentajePagoATiempoM2','PorcentajePagoATiempoM1','numeroPagosPorCreditoM5','numeroPagosPorCreditoM4','numeroPagosPorCreditoM3','numeroPagosPorCreditoM2',
                        'numeroPagosPorCreditoM1','IndiceNumPagosM5','IndiceNumPagosM4','IndiceNumPagosM3','IndiceNumPagosM2','IndiceNumPagosM1','PagoRapidoM5','PagoRapidoM4',
                        'PagoRapidoM3','PagoRapidoM2','PagoRapidoM1','numPromesas','cumplidas','dias'
                        ]

        #Columns to be using in the prediction.
        columnasDeDF4 = ['Cliente_id','PorcentajePagoATiempoM5','PorcentajePagoATiempoM4','PorcentajePagoATiempoM3','PorcentajePagoATiempoM2','PorcentajePagoATiempoM1','IndiceNumPagosM5',
                        'IndiceNumPagosM4','IndiceNumPagosM3','IndiceNumPagosM2','IndiceNumPagosM1','PagoRapidoM5','PagoRapidoM4','PagoRapidoM3','PagoRapidoM2','PagoRapidoM1','IndiceDePromesas'
                        ]

        df = pd.DataFrame(columns = columnasDeDF3)
        clientesFilter,clienteID = [],[]
      
        try:
            #list of clients to be used in the algorithm.
            clientes = list(clientesAanalizar(processing_option,client_id_url).cliente)
            cliente_to_remove = ['7470579b-4ef2-11ed-8600-645d86ddcc29', '3a7ce8ee-4ef1-11ed-9067-645d86ddcc29','fd8b00af-4ef3-11ed-83c6-645d86ddcc29',
            '419fb620-4ef5-11ed-8ef2-645d86ddcc29']
            for i in cliente_to_remove:
                try:
                    clientes.remove(i)
                except:
                    pass
        except:
            pass    
                
        contador = 0
        for i in clientes:
            try:      
                #For each client the app history is called calling the clientHistory function.
                newRow2 = clientHistory(i)
                df.loc[df.shape[0]] = newRow2
                clientesFilter.append(i)
                clienteID.append(i)
            except:
                print("Cliente no tiene suficientes prestamos",i, contador)
        #HIstoral de promesas de cientes
        IndiceDePromesaslist = IndiceDePromesas(df)
        df['IndiceDePromesas'] = IndiceDePromesaslist
        df2 = df[columnasDeDF4]

        try:
            df2.pop('Cliente_id')
        except:
            pass
        
        '''
        Predictions are being done in this loop, the probability to be a 0, the probability to be a 1
        ad the predicted label are bein processed and added to the previusly declared arrays.
        '''
        prob0,prob1,default2 = [], [],[]
        for i in range(df2.shape[0]):
            default2.append(modelToUse.predict([np.array(list(df2.iloc[i,:]))]))
            prob0.append(modelToUse.predict_proba([np.array(list(df2.iloc[i,:]))])[0][0])
            prob1.append(modelToUse.predict_proba([np.array(list(df2.iloc[i,:]))])[0][1])

        listaProbabilidad = prob1
        zipbObj = zip(clientes,listaProbabilidad)
        respuesta = dict(zipbObj)  

        context = {
            'listaProbabilidad':listaProbabilidad
        }

        '''
        For loop to insert or update every client who has beening processed. The data modeling is managed by the django orm.
        '''
        for i in range(len(clientes)):            
            if len(CustomerAnalytics.objects.filter(client=clientes[i])) == 0:
                clienteObj = Clients.objects.get(id=clientes[i])
                paso = 0 
                while paso==0:
                    try:
                        newUUID = uuid.uuid1()
                        print(newUUID)
                        print(respuesta[clientes[i]])
                        newInstance = CustomerAnalytics(id = newUUID, client=clienteObj,default_probability=respuesta[clientes[i]]*100, created_at=now(),updated_at=now())
                        newInstance.save()
                        paso=1                        
                    except:                    
                        newUUID = uuid.uuid1()
                        newInstance = CustomerAnalytics(id = newUUID, client=clienteObj,default_probability=respuesta[clientes[i]]*100, created_at=now(),updated_at=now())
                        newInstance.save()
                        paso=1                                          
            else:
                try:
                    newScore = CustomerAnalytics.objects.get(client= clientes[i])
                    newScore.default_probability = respuesta[clientes[i]]*100
                    newScore.updated_at = now()
                    newScore.save()
                except:
                    print("Ocurrio un error con el cliente:", clientes[i])
          
        return HttpResponse(f'{respuesta}') 
        #return render(request, 'classifier/home.html',context)


'''
Defualt Score class to serialize the objects from the data model.
Extends the views class
'''
class DefaultScore(viewsets.ModelViewSet):
    queryset = CustomerAnalytics.objects.all()
    serializer_class  = ScoreSerializer




# class Landing(View):
#     def get(self,request, *args,**kwargs):        
#         return render(request,'',{})