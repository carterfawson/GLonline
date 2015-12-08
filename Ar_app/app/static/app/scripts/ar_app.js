﻿$(".grid-basic").bootgrid();

$(".grid-nosearch").bootgrid({
	    templates: {
		        search: ""
		    }
});

﻿$(".grid-basic-cus").bootgrid({
	formatters: {
		"link": function (column, row) {
			return "<a href='" + jobUrl + "'>" + cusName + "</a>";
		}
	}
});

﻿$(".modal-body label").addClass("col-md-3 field-label");
