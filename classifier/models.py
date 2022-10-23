from django.db import models
from django.db import connections

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class ActivityLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    log_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField()
    subject_type = models.CharField(max_length=191, blank=True, null=True)
    subject_id = models.CharField(max_length=36, blank=True, null=True)
    causer_type = models.CharField(max_length=191, blank=True, null=True)
    causer_id = models.PositiveBigIntegerField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_log'


class Answers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class AnswersHistory(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers_history'


class ApprovedLoans(models.Model):
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    loan_approval_reason = models.ForeignKey('LoanApprovalReasons', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approved_loans'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlockingReasons(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    is_block = models.IntegerField()
    is_active = models.IntegerField()
    temporary = models.IntegerField()
    notification = models.ForeignKey('Notifications', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blocking_reasons'


class ClientAi(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    front_document = models.TextField()
    back_document = models.TextField()
    first_photo = models.TextField()
    second_photo = models.TextField()
    third_photo = models.TextField()
    accuracy = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    id_onboarding = models.CharField(max_length=191, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_ai'


class ClientComments(models.Model):
    content = models.TextField()
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_comments'


class ClientData(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    content = models.TextField()
    type = models.CharField(max_length=191)
    identifier = models.CharField(max_length=191, blank=True, null=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_data'


class ClientFiles(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    description = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_files'


class ClientFilesDetails(models.Model):
    client_file = models.ForeignKey(ClientFiles, models.DO_NOTHING)
    file_category = models.ForeignKey('FileCategories', models.DO_NOTHING)
    file_url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_files_details'


class ClientHistoryLocks(models.Model):
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    loan = models.ForeignKey('Loans', models.DO_NOTHING, blank=True, null=True)
    blocking_reason = models.ForeignKey(BlockingReasons, models.DO_NOTHING, blank=True, null=True)
    locked_date = models.DateTimeField(blank=True, null=True)
    unlocked_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_history_locks'


class ClientInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=191)
    dui = models.CharField(unique=True, max_length=191)
    nit = models.CharField(max_length=191)
    birth_date = models.DateField()
    gender = models.CharField(max_length=191)
    address = models.TextField()
    city = models.CharField(max_length=191)
    alternative_number_phone = models.CharField(max_length=191, blank=True, null=True)
    promotional_code = models.CharField(max_length=191, blank=True, null=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_info'


class ClientLevelHistory(models.Model):
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    previous_level = models.ForeignKey('Levels', on_delete=models.CASCADE, related_name="Client_Level_History_Previous_Level")
    next_level = models.ForeignKey('Levels', on_delete=models.CASCADE, related_name="Client_Level_History_Next_Level")
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_level_history'


class ClientLevelLoanHistory(models.Model):
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    current_level = models.ForeignKey('Levels', on_delete=models.CASCADE, related_name='Client_Level_Loan_History_Current_Level')
    requested_level = models.ForeignKey('Levels', on_delete=models.CASCADE, related_name='Client_Level_Loan_History_Requested_Level')
    amount = models.IntegerField()
    requested_at = models.DateTimeField()
    overdue_installments_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_level_loan_history'


class ClientLoanScores(models.Model):
    client_id = models.CharField(max_length=36)
    loan_id = models.CharField(max_length=36)
    score = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    risk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_approved = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_loan_scores'


class ClientNumberPhoneHistory(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    previous_number_phone = models.CharField(max_length=191)
    next_number_phone = models.CharField(max_length=191)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_number_phone_history'


class ClientScoreEntities(models.Model):
    client_id = models.CharField(max_length=36)
    client_score = models.ForeignKey('ClientScores', models.DO_NOTHING)
    entity_name = models.CharField(max_length=255, blank=True, null=True)
    line_type = models.CharField(max_length=255, blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    term_type = models.CharField(max_length=255, blank=True, null=True)
    term_status = models.CharField(max_length=255, blank=True, null=True)
    balance_status = models.CharField(max_length=255, blank=True, null=True)
    installment_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    due_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    due_days = models.IntegerField(blank=True, null=True)
    category_1 = models.CharField(max_length=255, blank=True, null=True)
    category_2 = models.CharField(max_length=255, blank=True, null=True)
    collateral = models.CharField(max_length=255, blank=True, null=True)
    last_payment_date = models.DateTimeField(blank=True, null=True)
    grant_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_score_entities'


class ClientScores(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    client_id = models.CharField(max_length=36)
    score = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    risk = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    message = models.CharField(max_length=300, blank=True, null=True)
    scored_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_scores'


class ClientSpecialDataBaseInfo(models.Model):
    special_data_base_info = models.ForeignKey('SpecialDataBaseInfo', models.DO_NOTHING)
    client = models.ForeignKey('Clients', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client_special_data_base_info'


class ClientTokenVerifications(models.Model):
    client = models.ForeignKey('Clients', models.DO_NOTHING)
    token = models.CharField(max_length=191)
    expires_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_token_verifications'


class Clients(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    number_phone = models.CharField(unique=True, max_length=191)
    invitation_code = models.CharField(max_length=191)
    level = models.ForeignKey('Levels', models.DO_NOTHING)
    level_at = models.DateField()
    loans_requested = models.IntegerField()
    verified = models.IntegerField()
    notify = models.IntegerField()
    special = models.IntegerField()
    status = models.CharField(max_length=191)
    block_at = models.DateField(blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    unlocked_at = models.DateTimeField(blank=True, null=True)
    ocr_verified = models.IntegerField()
    bo_verified = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class CustomerAnalytics(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    default_probability = models.DecimalField(max_digits=10, decimal_places=3)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_analytics'


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    iso_code = models.CharField(unique=True, max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Devices(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    token = models.TextField()
    client_id = models.CharField(max_length=36)
    client_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Faq(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    question = models.CharField(max_length=191)
    answer = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faq'


class FileCategories(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=400)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_categories'


class InvoiceTransactionTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    code = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_transaction_types'


class InvoiceTransactions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    invoice_type = models.ForeignKey('InvoiceTypes', models.DO_NOTHING)
    installment_number = models.IntegerField(blank=True, null=True)
    invoice_transaction_type = models.ForeignKey(InvoiceTransactionTypes, models.DO_NOTHING)
    commission_amount = models.IntegerField()
    commission_tax = models.IntegerField()
    interest_amount = models.IntegerField()
    interest_tax = models.IntegerField()
    overdue_amount = models.IntegerField()
    overdue_tax = models.IntegerField()
    invoiced_at = models.DateField()
    reversed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_transactions'


class InvoiceTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    code = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'invoice_types'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=191)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class LevelAmounts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    amount = models.BigIntegerField()
    level = models.ForeignKey('Levels', models.DO_NOTHING)
    available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level_amounts'


class LevelPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.ForeignKey('Levels', models.DO_NOTHING)
    period = models.ForeignKey('Periods', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'level_period'


class Levels(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    image = models.CharField(max_length=191, blank=True, null=True)
    order = models.IntegerField()
    commission = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=8, decimal_places=2)
    due_rate = models.DecimalField(max_digits=8, decimal_places=2)
    min_loans = models.IntegerField()
    min_time = models.IntegerField()
    normal = models.IntegerField()
    special = models.IntegerField()
    active = models.IntegerField()
    require_minimum_amount = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levels'


class LoanApprovalReasons(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    is_active = models.IntegerField()
    notification = models.ForeignKey('Notifications', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_approval_reasons'


class LoanDetailUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    loan_detail = models.ForeignKey('LoanDetails', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_detail_user'


class LoanDetails(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    number_fee = models.IntegerField()
    amount = models.BigIntegerField()
    balance = models.BigIntegerField()
    principal_amount = models.BigIntegerField(blank=True, null=True)
    interest_amount = models.BigIntegerField(blank=True, null=True)
    iva_interest_amount = models.BigIntegerField(blank=True, null=True)
    due = models.BigIntegerField()
    debt_paid = models.BigIntegerField(blank=True, null=True)
    paid = models.BigIntegerField()
    status = models.IntegerField()
    expire_at = models.DateField()
    paid_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_details'


class LoanDueRemovals(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    due = models.FloatField()
    installment_number = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_due_removals'


class LoanPenalties(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    days_in_arrears = models.IntegerField()
    days_to_block = models.IntegerField()
    block_client = models.IntegerField()
    is_temporary_block = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_penalties'


class LoanReferrals(models.Model):
    referred_loan = models.ForeignKey('Loans', on_delete=models.CASCADE, related_name='Loan_Referrals_Refferred_Loan')
    referring_loan = models.ForeignKey('Loans', on_delete=models.CASCADE, related_name='Loan_Referrals_Referring_Loan', blank=True, null=True)
    referral = models.ForeignKey('Referrals', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_referrals'


class LoanRejectionReasons(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    is_active = models.IntegerField()
    block = models.IntegerField()
    code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    notification = models.ForeignKey('Notifications', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_rejection_reasons'


class LoanRepayments(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    payment_detail = models.ForeignKey('PaymentDetails', models.DO_NOTHING)
    installment_number = models.IntegerField()
    principal_amount = models.BigIntegerField()
    interest_amount = models.BigIntegerField()
    interest_tax_amount = models.BigIntegerField()
    overdue_amount = models.BigIntegerField()
    overdue_tax_amount = models.BigIntegerField()
    balance = models.BigIntegerField()
    balance_available = models.BigIntegerField()
    refund_amount = models.BigIntegerField()
    repayment_date = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_repayments'


class LoanReversals(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    comment = models.CharField(max_length=500)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    reversal_type = models.ForeignKey('ReversalTypes', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_reversals'


class LoanTigoMoneyDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    tigo_money_detail = models.ForeignKey('TigoMoneyDetails', models.DO_NOTHING)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'loan_tigo_money_detail'


class Loans(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    identifier = models.CharField(max_length=191, blank=True, null=True)
    correlative = models.CharField(max_length=191, blank=True, null=True)
    amount = models.BigIntegerField()
    commission = models.BigIntegerField(blank=True, null=True)
    installment_amount = models.BigIntegerField(blank=True, null=True)
    interest = models.BigIntegerField(blank=True, null=True)
    iva_interest = models.BigIntegerField(blank=True, null=True)
    period_name = models.CharField(max_length=191, blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    repeat = models.IntegerField(blank=True, null=True)
    year_rate = models.FloatField(blank=True, null=True)
    iva_rate = models.FloatField(blank=True, null=True)
    applied_percentage = models.BigIntegerField()
    due_rate = models.FloatField(blank=True, null=True)
    wallet = models.ForeignKey('Wallets', models.DO_NOTHING)
    comment = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    is_blocked = models.IntegerField(blank=True, null=True)
    accepted_at = models.DateTimeField(blank=True, null=True)
    due_at = models.DateField(blank=True, null=True)
    score_granted_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loans'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=191)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=191)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class Municipalities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    nit_code = models.CharField(unique=True, max_length=191)
    postal_code = models.CharField(max_length=191)
    department = models.ForeignKey(Departments, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipalities'


class Notifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField()
    type = models.IntegerField()
    params = models.CharField(max_length=10, blank=True, null=True)
    sms = models.IntegerField()
    push = models.IntegerField()
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class Options(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    text = models.CharField(max_length=191)
    order = models.IntegerField(blank=True, null=True)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PaymentDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    record_n = models.CharField(max_length=191, blank=True, null=True)
    company_code = models.CharField(max_length=191, blank=True, null=True)
    reference = models.CharField(max_length=191, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    payment_date = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    msisdn = models.CharField(max_length=191, blank=True, null=True)
    process_status = models.IntegerField(blank=True, null=True)
    payment = models.ForeignKey('Payments', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_details'


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=191)
    expected_amount = models.BigIntegerField(blank=True, null=True)
    advance_amount = models.BigIntegerField(blank=True, null=True)
    processed_due = models.BigIntegerField(blank=True, null=True)
    expected_due = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class PeriodSettings(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    min_days = models.IntegerField()
    max_days = models.IntegerField(blank=True, null=True)
    fee = models.IntegerField()
    period = models.ForeignKey('Periods', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'period_settings'


class PeriodTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    value = models.IntegerField()
    days_to_add = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'period_types'


class Periods(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    days = models.CharField(max_length=191, blank=True, null=True)
    repeat = models.IntegerField()
    period_type = models.ForeignKey(PeriodTypes, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periods'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Questions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    text = models.TextField()
    type = models.CharField(max_length=191)
    for_field = models.CharField(db_column='for', max_length=191, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    required = models.IntegerField()
    max_length = models.IntegerField(blank=True, null=True)
    mode = models.CharField(max_length=8)
    validation_endpoint = models.CharField(max_length=191, blank=True, null=True)
    step = models.ForeignKey('Steps', models.DO_NOTHING)
    order = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class QuotePayments(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.BigIntegerField()
    due = models.BigIntegerField()
    residue = models.BigIntegerField()
    loan_detail = models.ForeignKey(LoanDetails, models.DO_NOTHING)
    payment_detail = models.ForeignKey(PaymentDetails, models.DO_NOTHING)
    paid_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_payments'


class Referrals(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    referring_client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='Referrals_Referring_Client')
    referred_client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='Referrals_Referred_Client')
    percentage_to_apply = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referrals'


class RejectedLoans(models.Model):
    loan = models.ForeignKey(Loans, models.DO_NOTHING)
    loan_rejection_reason = models.ForeignKey(LoanRejectionReasons, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rejected_loans'


class RepaymentPartTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    code = models.CharField(max_length=191)
    order = models.IntegerField(unique=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repayment_part_types'


class ReversalTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    code = models.CharField(max_length=191)
    name = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'reversal_types'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class ScoreCategories(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=25)
    from_days = models.IntegerField()
    to_days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score_categories'


class Settings(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    year_rate = models.FloatField()
    due_rate = models.FloatField()
    iva_rate = models.FloatField()
    referral_percentage = models.IntegerField()
    referring_percentage = models.IntegerField()
    maximum_referral_percentage = models.IntegerField()
    period_grace = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class SpecialDataBaseInfo(models.Model):
    person_code = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    phone_number = models.CharField(max_length=191, blank=True, null=True)
    dui = models.CharField(db_column='DUI', max_length=191, blank=True, null=True)  # Field name made lowercase.
    nit = models.CharField(db_column='NIT', max_length=191, blank=True, null=True)  # Field name made lowercase.
    registered = models.IntegerField()
    special_data_base = models.ForeignKey('SpecialDataBases', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_data_base_info'


class SpecialDataBases(models.Model):
    name = models.CharField(unique=True, max_length=191)
    level = models.ForeignKey(Levels, models.DO_NOTHING)
    priority = models.IntegerField(blank=True, null=True)
    characteristics = models.CharField(max_length=191, blank=True, null=True)
    active = models.IntegerField()
    automatic = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=12)
    pattern = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_data_bases'


class Steps(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(unique=True, max_length=191)
    order = models.PositiveIntegerField(unique=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'steps'


class SubTicketTypeFields(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=250)
    source = models.JSONField(blank=True, null=True)
    source_origin = models.CharField(max_length=8, blank=True, null=True)
    default_value = models.JSONField(blank=True, null=True)
    default_value_origin = models.CharField(max_length=9, blank=True, null=True)
    others = models.IntegerField()
    required = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    mask = models.CharField(max_length=250, blank=True, null=True)
    sub_ticket_type_option = models.ForeignKey('SubTicketTypeOptions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_ticket_type_fields'


class SubTicketTypeOptions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True, null=True)
    order = models.IntegerField()
    type = models.CharField(max_length=5)
    active = models.IntegerField()
    compare_values = models.IntegerField()
    sub_ticket_type = models.ForeignKey('SubTicketTypes', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_ticket_type_options'


class SubTicketTypeValues(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    value = models.TextField(blank=True, null=True)
    resolved = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
    sub_ticket_type_field = models.ForeignKey(SubTicketTypeFields, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_ticket_type_values'


class SubTicketTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    active = models.IntegerField()
    notify = models.IntegerField()
    ticket_type = models.ForeignKey('TicketTypes', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_ticket_types'


class SystemNotifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=191)
    notifiable_type = models.CharField(max_length=191)
    notifiable_id = models.PositiveBigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_notifications'


class TicketFollowers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_followers'


class TicketLoanInstallments(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
    installment = models.ForeignKey(LoanDetails, models.DO_NOTHING)
    pending_installment_amount = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_loan_installments'


class TicketReminderTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    code = models.CharField(max_length=191)
    order = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'ticket_reminder_types'


class TicketResultTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    code = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'ticket_result_types'


class TicketStatuses(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=250)
    order = models.IntegerField()
    code = models.CharField(unique=True, max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_statuses'


class TicketTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=191)
    code = models.CharField(max_length=191)
    management = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ticket_types'


class Tickets(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    assigned_by = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='Tickets_Assigned_by', db_column='assigned_by', blank=True, null=True)
    assigned_to = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='Tickets_Assigned_to', db_column='assigned_to', blank=True, null=True)
    loan = models.ForeignKey(Loans, models.DO_NOTHING, blank=True, null=True)
    ticket_type = models.ForeignKey(TicketTypes, models.DO_NOTHING)
    ticket_result_type = models.ForeignKey(TicketResultTypes, models.DO_NOTHING, blank=True, null=True)
    ticket_reminder_type = models.ForeignKey(TicketReminderTypes, models.DO_NOTHING, blank=True, null=True)
    ticket_status = models.ForeignKey(TicketStatuses, models.DO_NOTHING, blank=True, null=True)
    sub_ticket_type = models.ForeignKey(SubTicketTypes, models.DO_NOTHING, blank=True, null=True)
    phone_number = models.CharField(max_length=191, blank=True, null=True)
    reference_code = models.CharField(max_length=191, blank=True, null=True)
    reminded_at = models.DateTimeField(blank=True, null=True)
    reminder_date = models.DateField(blank=True, null=True)
    reminder_time = models.TimeField(blank=True, null=True)
    expires_at = models.DateField(blank=True, null=True)
    total_pending_amount = models.BigIntegerField(blank=True, null=True)
    promised_payment_amount = models.BigIntegerField(blank=True, null=True)
    comment = models.CharField(max_length=1500, blank=True, null=True)
    promise_status = models.CharField(max_length=9, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class TigoMoney(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    n_account = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    min_amount = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tigo_money'


class TigoMoneyDetails(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    tigo_money = models.ForeignKey(TigoMoney, models.DO_NOTHING)
    amount = models.BigIntegerField()
    balance = models.BigIntegerField()
    incoming = models.IntegerField()
    type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tigo_money_details'


class Users(models.Model):
    name = models.CharField(max_length=191)
    username = models.CharField(unique=True, max_length=191)
    email = models.CharField(unique=True, max_length=191)
    password = models.CharField(max_length=191)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class WalletBrands(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(unique=True, max_length=191)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_brands'


class Wallets(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    number_account = models.CharField(max_length=191)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    wallet_brand = models.ForeignKey(WalletBrands, models.DO_NOTHING)
    verified = models.IntegerField()
    active = models.IntegerField()
    opened_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallets'


#clientesAAnalizar = Loans.objects.filter(id=1).select_related() 