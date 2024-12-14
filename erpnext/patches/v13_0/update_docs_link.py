# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE


import frappe


def execute():
	navbar_settings = frappe.get_single("Navbar Settings")
	for item in navbar_settings.help_dropdown:
		if item.is_standard and item.route == "https://psmnext.com/docs/user/manual":
			item.route = "https://docs.psmnext.com/docs/v14/user/manual/en/introduction"

	navbar_settings.save()
