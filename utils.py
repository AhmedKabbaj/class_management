from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo import models, fields, api, _



def get_months_between(start_date, end_date):
    # List to store the months
    months = []

    # Loop through each month between start_date and end_date
    current_date = start_date
    while current_date <= end_date:
        months.append(str(current_date.month).zfill(2))
        current_date += relativedelta(months=1)
    return months


def get_school_year(env):
    return env['center.school_year'].search([], order="create_date desc", limit=1)

def get_unpaid_months(env,rec):
    start_date = rec.date_start
    end_date = fields.Date.today()
    unpaid_months = []

    if start_date:
        print('inside date start --------------------------vvvvv')
        months = get_months_between(start_date, end_date)
        for month in months:
            payment = env['center.payment'].search([
                ('subscription_service_id', '=', rec.id), 
                ('month', '=', month)    
            ])
            if not payment:
                unpaid_months.append(month)
    return unpaid_months


def calcule_unpaid_months(env, subscribe):
    amount = 0
    for service in subscribe.cycle_level_service_ids:
        amount += service.price * len(get_unpaid_months(env, service))

    return amount