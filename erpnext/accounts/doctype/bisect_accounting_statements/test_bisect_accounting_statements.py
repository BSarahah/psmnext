# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestBisectAccountingStatements(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestBisectAccountingStatements(UnitTestCase):
	"""
	Unit tests for BisectAccountingStatements.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestBisectAccountingStatements(IntegrationTestCase):
>>>>>>> ee9a2952d6 (fix: switched asset terminology from cost to value)
	pass
