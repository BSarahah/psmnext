frappe.listview_settings["Code List"] = {
	onload: function (listview) {
		listview.page.add_inner_button(__("Import Genericode File"), function () {
			psmnext.edi.import_genericode(listview);
		});
	},
	hide_name_column: true,
};
