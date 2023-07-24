import frappe
from frappe.utils  import flt

def set_item_attributes(self, method):
    attr_list = ["Width", "Height", "Yield"]
    if self.variant_of:
        if self.attributes:
            for attr in self.attributes:
                if attr.attribute in attr_list:
                    if attr.attribute == "Yield":
                        atr = "Yield_Num"
                        self.db_set(atr.lower(), attr.attribute_value)
                    else:        
                        atr = attr.attribute
                        self.db_set(atr.lower(), attr.attribute_value)
            

def get_conv_factor_value(self, method):
    data = {"yield_num": flt(self.yield_num) if self.yield_num else 1, "length": flt(self.length) if self.length else 1, "width": flt(self.width) if self.width else 1, "height": flt(self.height) if self.height else 1}
    if self.uoms:
        for cf in self.uoms:
            if cf.uom and cf.formula:
                value = frappe.safe_eval(cf.formula, None, data)
                cf.conversion_factor = value