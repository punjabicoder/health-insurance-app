from django.test import TestCase
from .models import InsurancePlan

class InsurancePlanTest(TestCase):
    def test_plan_creation(self):
        plan = InsurancePlan.objects.create(
            name = "Basic Plan",
            premium = 100.00,
            coverage = "Hospital + Dental"
        )
        self.assertEqual(plan.name, "Basic Plan")

# Create your tests here.
