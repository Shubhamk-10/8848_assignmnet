import frappe

def set_item_attributes(self, method):
    attr_list = ["Width", "Height", "Yield"]
    if self.variant_of:
        if self.attributes:
            for attr in self.attributes:
                if attr.attribute in attr_list:
                    if attr.attribute == "Yield":
                        atr = "Yield_Num"
                        self.db_set(atr.lower(), attr.attribute_value)
                    atr = attr.attribute
                    self.db_set(atr.lower(), attr.attribute_value)
            

def get_conv_factor_value(self, method):
    data = {"yield_num": float(self.yield_num), "length": float(self.length), "width": float(self.width), "height": float(self.height)}
    if self.uoms:
        for cf in self.uoms:
            if cf.uom and cf.formula:
                value = frappe.safe_eval(cf.formula, None, data)
                cf.conversion_factor = value