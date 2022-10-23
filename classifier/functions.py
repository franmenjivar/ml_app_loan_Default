from django.db import connection
import pandas as pd
from datetime import datetime, date

'''
function class containing all the functions used by the views
@Author Erick
'''

'''
days_between function returns the differences between two days named int d1 and int d2
@Parameters d1, d2
'''
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def clientesAanalizar(processing_option,client_id_url):
    option = processing_option
    if option == 'global_search':
        query = f'''    
        select wallets.client_id as cliente from wallets 
        left join loans on loans.wallet_id = wallets.id 
        where client_id = '{client_id_url}'
        '''
        #'9086f1c9-9f54-420f-8e0d-0b8c6b85d635'

    elif option == 'allavailablecustumers':
        # query = '''     
        # select distinct(cliente) from (select wallets.client_id as cliente from wallets 
        # left join loans on loans.wallet_id = wallets.id where amount >= 7000 and  loans.accepted_at>'2021-06-30') as y         
        # '''    
        query = '''
        SELECT client_id as cliente FROM diimo_core.customer_analytics
        '''
    elif option == 'specificavilablecustomer':
        query = f'''     
        select distinct(cliente) from (select wallets.client_id as cliente from wallets 
        left join loans on loans.wallet_id = wallets.id where amount >= 7000 and  loans.accepted_at>'2021-06-30') as y   
        where cliente = '{client_id_url}'
        '''
    df = pd.read_sql(query, connection)            
    return df


def PrestamosAAnalizar(client_id):
    query = f'''
        SELECT  diimo_core.loans.id as loanID, accepted_at FROM diimo_core.loans
        left join (select id,client_id from diimo_core.wallets)as X on diimo_core.loans.wallet_id = X.id
        left join (SELECT client_id FROM diimo_core.client_info) as Y on X.client_id = Y.client_id
        where X.client_id= "{client_id}" and accepted_at is not null
        order by accepted_at asc;
        '''
    df = pd.read_sql(query, connection)
    return df

def cuotasPorPrestamo(loan_id):
    query = f'''
        SELECT loan_id, number_fee, amount, expire_at, paid_at, ifnull(datediff(paid_at,expire_at),999999) as difDias,datediff(current_date(),expire_at) as diasPostPago,created_at FROM diimo_core.loan_details
        where loan_id = '{loan_id}'
        order by number_fee asc;
        '''
    df = pd.read_sql(query, connection)
    return df

def promesas(loan_id):
    listaPromesas, cumplidas = 0, 0
    query = f'''
        SELECT promise_status FROM diimo_core.tickets
        where expires_at is not null and loan_id = '{loan_id}'
        '''
    df = pd.read_sql(query, connection)

    if df.shape[0] !=0:
        cumplidas = list(df.promise_status).count('Cumplida')
        listaPromesas = df.shape[0]

    return listaPromesas, cumplidas

def detallesPrestamo(prestamo):
    dueDate = list(prestamo.expire_at)
    estadoCuota = list(prestamo.paid_at)
    diffDias = list(prestamo.difDias)
    diasPostPago = list(prestamo.diasPostPago)
    return dueDate,estadoCuota,diffDias, diasPostPago

def clientHistory(client_id):
    newRow = []
    numCuotasPrestamo,cuotasPagadasATiempoTotal = [],[]
    prestamos = PrestamosAAnalizar(client_id)
    idsPrestamos = list(prestamos.loanID)
    fechaAceptacionCreditos = list(prestamos.accepted_at)
    porcentajePago = []
    pagoRapidoDeCredito = []
    numeroPagosPorCredito = []
    IndiceNumPagos = []
        
    for prestamo in reversed(range(1,6)):
        cuotasPagadasATiempo = []        
        setCuotas = len(set(cuotasPorPrestamo(list(prestamos.loanID)[-prestamo]).paid_at))
        listaCuotas = len(list(cuotasPorPrestamo(list(prestamos.loanID)[-prestamo]).paid_at))
        
        try:
            IndiceNumPagos.append(abs((setCuotas/listaCuotas)-1))
        except:
            print("problem with IndiceNumPagos")
        
        try:
            numeroPagosPorCredito.append(setCuotas)
        except:
            print("Problem in numero de pagos")
            
        try:
            dias = (list(prestamos.accepted_at)[-prestamo]-list(prestamos.accepted_at)[-prestamo-1]).days            
        except:            
            dias = 0        
            
        idLoan,estadoCuotaPrestamoAnterior, diferenciaDeDias = idsPrestamos[-prestamo],[],[]
        prestamoDetail = cuotasPorPrestamo(idLoan)
        fechaUltimoPago = list(prestamoDetail.paid_at)[-1]
        
        try:
            diasAcceptedPagadoVar = days_between(str(fechaUltimoPago), str(fechaAceptacionCreditos[-prestamo])[:10])
            if diasAcceptedPagadoVar <=5:
                diasAcceptedPagadoRapido = 1
            else:
                diasAcceptedPagadoRapido = 0                          
        except:
            diasAcceptedPagadoRapido = 0
            
        pagoRapidoDeCredito.append(diasAcceptedPagadoRapido)      
        numCuotasPrestamo.append(prestamoDetail.shape[0])
        dueDate,estadoCuota,diffDias,diasPostPago = detallesPrestamo(prestamoDetail)

        # Estados 1 = Pagado, 0=Pendiente de pago
        for cuota in reversed(range(1,13)):
            
            try:                
                if estadoCuota[-cuota] != None:                    
                    if diffDias[-cuota]<=0:
                        cuotasPagadasATiempo.append(1)
                    diferenciaDeDias.append(diffDias[-cuota])
                else:
                    if dueDate[-cuota]>date.today():
                        diferenciaDeDias.append(diasPostPago[-cuota])
                    elif dueDate[-cuota] == date.today():
                        diferenciaDeDias.append(0)
                    else:
                        diferenciaDeDias.append(diasPostPago[-cuota])         
            except:
                diferenciaDeDias.append(0)
                
            try:
                if estadoCuota[-cuota] != None:
                    estadoCuotaPrestamoAnterior.append(1)
                else:
                    estadoCuotaPrestamoAnterior.append(0)
            except:
                estadoCuotaPrestamoAnterior.append(1)
                
        cuotasPagadasATiempoTotal.append(sum(cuotasPagadasATiempo))
        numPromesas, cumplidas = promesas(idLoan)
        porcentajePago.append(abs((cuotasPagadasATiempoTotal[-1]/numCuotasPrestamo[-1])-1))
        newRow = [client_id]+numCuotasPrestamo + cuotasPagadasATiempoTotal+porcentajePago+numeroPagosPorCredito+IndiceNumPagos +pagoRapidoDeCredito + [numPromesas] + [cumplidas] + [dias]
    
    if len(newRow) != 34:
        print("Error in the lenght")
    return newRow

def IndiceDePromesas(df):
    IndiceDePromesas = []
    for i in range(df.shape[0]):
        if list(df.numPromesas)[i]!=0:
            IndiceDePromesas.append(abs((list(df.cumplidas)[i]/list(df.numPromesas)[i])-1))
        else:
            IndiceDePromesas.append(0)
    return IndiceDePromesas
