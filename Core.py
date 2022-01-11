import re

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- 
# | Pen-OS Script Project         |
# |                               |
# |                               |
# |                               |
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#To support the creation of commands

### Will be used for the input loop


def policy_or_object():
	type = ""
	type = input ("Choose either policy (P) or object (O): ")
	if type == "P":
		print ("Policy has been selected")
		return type
		break
	elif type == "O":
		print ("Object has been selected")
		return type
		break
	else:
		print ("This is an incorrect value, enter P for policy or O for object")
		continue


class PolicyInformation:

	def __init__(self):

		### Triage ####################################################

		self.new_edit = input ("Are you creating a new policy (N) or editing an existing one (E): ")
		self.policy = \

		input("""
		1) Security
		2) NAT
		3) QoS
		4) Policy Based Forwarding
		5) Decryption
		6) Tunnel Inspection
		7) Application Override
		8) Authentication
		9) DoS Protection

		Select the appropriate number : """)

		### Default policy #############################################

		self.rulename = ["rulename",input ("Enter the rulename : ")]
		self.description = ["description",input ("Enter the description : ")]
		self.tags = ["tags",input ("List your tag(s): ")]
		self.group = ["group",input ("List your group(s): ")]
		self.src_zone = ["src_zone",input ("List your zone(s): ")]
		self.src_address = ["src_address",input ("List your source address(es:) ")]
		self.dst_zone = ["dst_zone",input ("List your destination zone(s): ")]
		self.dst_address = ["dst_address",input ("List your destination address(es): ")]	
		self.service = ["service",input ("List your service(s): ")]
		self.default_policy = []

		### Default security ###########################################

		self.type = ["type",input ("Enter the rule type: ")]
		self.src_hip = ["src_hip",input ("List your source hip(s): ")]
		self.src_user = ["src_user",input ("List your source user(s): ")]
		self.application = ["application",input ("List your application(s): ")]
		self.action = ["action",input ("Enter the action: ")]
		self.profile_type = ["profile_type",input ("Enter the profile type (group/profile/none): ")]
		self.profile_group = ["profile_group",input ("Enter the profile group: ")]
		self.profiles = ["profiles",input ("List the profiles: ")]
		self.url_category = ["url_category",input ("List your url categories: ")]
		self.default_security = []

		### Default NAT #################################################

		self.dst_interface = ["dst_interface",input ("Enter the destination interface (Or leave empty for any): ")]
		self.src_translation_mode = ["src_translation",input ("Select translation mode (static/dynamic/dynamic IP and Port: ")]
		self.src_translation_address = ["src_translation_address",input ("Enter the source translation address (Or leave empty for any): ")]
		self.src_translation_direction = ["src_translation_direction",input ("Is the translation bi-directional (Y/N): ")]
		self.dst_translation_mode = ["dst_translation_mode",input ("Select translation mode (static/dynamic/dynamic IP and Port (Or leave empty for any): ")]
		self.dst_translation_address = ["dst_translation_address",input ("Enter the destination translation address (Or leave empty for any): ")]
		self.dst_translation_direction = ["dst_translation_direction",input ("Is the translation bi-directional (Y/N): ")]
		self.default_NAT = []

		### Default QOS ##################################################

		self.DSCPTos = ["DSCPTos",input ("Any or Codepoints: ")]
		self.cl_ass = ["class",input ("Enter the class: ")]
		self.default_QOS = []

		### Default PBF ##################################################

		self.egress_interface = ["egress_interface",input ("Enter the egress interface (Or leave empty for none): ")]
		self.next_hop = ["next_hop",input ("Enter the next hop (Or leave empty for none)": )]
		self.symmetric_return = ["symmetric_return",input ("Do you want symmetric return to be enforced (Y/N): ")]
		self.schedule = ["schedule",input ("Enter the schedule (Or leave empty for none): ")]
		self.default_PBF = []

	def organize_information():
		
		

def building_policy(Information):

### Common 
	
	Information = PolicyInformation
	string_attributes = ["description","tag","from"."source","destination","source-user","category","application","service","hip-profiles","action","rule-type",\
	"to","group-tag","profile-setting"]

### Set settings

	set_security_string = "set rulebase security rules"
	set_NAT_string = "set rulebase nat rules"
	set_PBF_string = "set rulebase pbf rules"
	set_QOS_string = "set rulebase qos rules"

### Delete settings

	dlt_security_string = "delete rulebase security rules"
	dlt_NAT_string = "delete rulebase nat rules"
	dlt_PBF_string = "delete rulebase pbf rules"
	dlt_QOS_string = "delete rulebase qos rules"
	

	if Information.new_edit == "N":
		for i in current_build:
			print ({set_string}, {Information.rulename}, {string_attributes[i]}, sep=' ', '\n')


class ObjectInformation:
	object_type = input ("Please enter the object type: ")



def building_objects(Information):
	Information = ObjectInformation








if int(Policy_Type) == 1:
	print(f"\nset audit-comment xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/security/rules/entry[@name='{PreRulename}'] comment {PreComment}\n")
elif int(Policy_Type) == 2:
	print(f"\nset audit-comment xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/nat/rules/entry[@name='{PreRulename}'] comment {PreComment}\n")
else:
	print(f"\nset audit-comment xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/qos/rules/entry[@name='{PreRulename}'] comment {PreComment}\n")

	# Send_String = (f"\nset audit-comment xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/{Policy_Type}/rules/entry[@name='{Rulename}'] comment {Comment}\n")
