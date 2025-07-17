from django.db import models

class EmployeeMaster(models.Model):
    Employee_name = models.TextField()
    audit_manager = models.TextField(blank=True, null=True)
    Partner = models.TextField(blank=True, null=True)
    Admin = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'employee_master'
        managed = True

    def __str__(self):
        return f"Employee_name: {self.Employee_name}, audit_manager: {self.audit_manager}, Partner: {self.Partner}, Admin: {self.Admin}"


class ClientMaster(models.Model):
    Client_name = models.TextField()
    audit_manager = models.TextField(blank=True, null=True)
    Partner  = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'client_master'
        managed = True

    def __str__(self):
        return f"Client_name: {self.Client_name}, Audit Manager: {self.audit_manager}, Partner: {self.Partner}"


class Users(models.Model):
    Username = models.TextField()
    Password = models.TextField()

    class Meta:
        db_table = 'users'
        managed = True

    def __str__(self):
        return f"Username: {self.Username}, Password: {self.Password}"


class Planning(models.Model):
    date = models.DateField()
    employee_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    fullday_halfday = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'planning'
        managed = True

    def __str__(self):
        return f"Date: {self.date}, Employee: {self.employee_name}, Client: {self.client_name}, Type: {self.fullday_halfday}, Description: {self.description}"
