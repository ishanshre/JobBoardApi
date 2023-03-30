from django.db import models


class SECTOR_SELECT(models.TextChoices):
    FINANCE = "Finance", 'Finance'
    INVESTMENT = "Investment", 'Investment'
    PRIVATE_SECTOR = "Private Sector", 'Private Sector'
    MANUFACTURING = "Manufacturing", 'Manufacturing'
    STOCK_MARKET = "Stock market", 'Stock market'
    LEGAL_SERVICES = "Legal Services", 'Legal Services'
    BANKING = "Banking", 'Banking'
    SOCIAL_WORK = "Social Work", 'Social Work'
    EDICATION = "Education", 'Education'
    RETAIL = "Retail", 'Retail'
    COMPUTER_AND_INFORMATION_TECHNOLOGY ="Computers and information technology", 'Computers and information technology'
    INSURANCE = "Insurance", 'Insurance'
    LOGISTICS = "Logistics", 'Logistics'
    MARKETING = "Marketing", 'Marketing'
    ACCOUNTING = "Accounting", 'Accounting'
    TELECOMMUNICATIONS = "Telecommunications", 'Telecommunications'
    HUMAN_RESOURCES = "Human Resources", 'Human Resources'
    CONSTRUCTION_INDUSTRY = "construction industry", 'construction industry'
    FOOD_INDUSTRY = "Food industry", 'Food industry'
    CUSTOMER_SERVICE = "Customer Service", 'Customer Service'
    PUBLIC_RELATION = "Public Relations", 'Public Relations'



class COMPANY_TYPE(models.TextChoices):
    PRIVATE = "Private", 'Private'
    PUBLIC = "Public", 'Public'
    NON_PROFIT_DISTRIBUTING = "Non-Profit Distributing", 'Non-Profit Distributing'