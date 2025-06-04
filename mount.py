class Mount():
    mount_id = -1
    mount_name = ""
    item_id = -1
    item_name = ""
    source = None

    def __init__(self, mount_id, mount_name, item_id, item_name, source):
        self.mount_id = mount_id
        self.mount_name = mount_name
        self.item_id = item_id
        self.item_name = item_name
        self.source = source

    def get_mount_id(self):
        return self.mount_id
        
    def get_mount_name(self):
        return self.mount_name
    
    def get_item_id(self):
        return self.item_id
    
    def get_item_name(self):
        return self.item_name
    
    def get_source(self):
        return self.source

class Source():
    category = ""

    def get_category(self):
        return self.category
    
class Achievement(Source):
    achievement_id = -1
    achievement_name = ""
    
    def __init__(self, category, achievement_id, achievement_name):
        self.category = category
        self.achievement_id = achievement_id
        self.achievement_name = achievement_name
    
    def get_achievement_id(self):
        return self.achievement_id
    
    def get_achievement_name(self):
        return self.achievement_name

class Drop(Source):
    instance_id = -1
    instance_name = ""
    encounter_id = -1
    encounter_name = ""

    def __init__(self, category, instance_id, instance_name, encounter_id, encounter_name):
        self.category = category
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.encounter_id = encounter_id
        self.encounter_name = encounter_name

    def get_instance_id(self):
        return self.instance_id
    
    def get_instance_name(self):
        return self.instance_name
    
    def get_encounter_id(self):
        return self.encounter_id
    
    def get_encounter_name(self):
        return self.encounter_name
