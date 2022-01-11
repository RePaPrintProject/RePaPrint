import re

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- 
# | Pen-OS Script Project         |
# |                               |
# |                               |
# |                               |
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Print audit comment for Palo Alto Networks

class information:

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

		self.rulename = input ("Enter the rulename : ")
		self.description = input ("Enter the comment : ")
		self.tags = input ("List your tag(s): ")
		self.group = input ("List your group(s): ")
		self.src_zone = input ("List your zone(s): ")
		self.src_address = input ("List your source address(es:) ")
		self.dst_zone = input ("List your destination zone(s): ")
		self.dst_address = input ("List your destination address(es): ")		
		self.service = input ("List your service(s): ")

		### Default security ###########################################

		self.type = input ("Enter the rule type: ")
		self.src_hip = input ("List your source hip(s): ")
		self.src_user = input ("List your source user(s): ")
		self.application = input ("List your application(s): ")
		self.action = input ("Enter the action: ")
		self.profile_type = input ("Enter the profile type (group/profile/none): ")
		self.profile_group = input ("Enter the profile group: ")
		self.profiles = input ("List the profiles: ")
		self.url_category = input ("List your url categories: ")

		### Default NAT #################################################

		self.dst_interface = input ("Enter the destination interface (Or leave empty for any): ")
		self.src_translation_mode = input ("Select translation mode (static/dynamic/dynamic IP and Port: ")
		self.src_translation_address = input ("Enter the source translation address (Or leave empty for any): ")
		self.src_translation_direction = input ("Is the translation bi-directional (Y/N): ")
		self.dst_translation_mode = input ("Select translation mode (static/dynamic/dynamic IP and Port (Or leave empty for any): ")
		self.dst_translation_address = input ("Enter the destination translation address (Or leave empty for any): ")
		self.dst_translation_direction = input ("Is the translation bi-directional (Y/N): ")

		### Default QOS ##################################################

		self.DSCPTos = input ("Any or Codepoints: ")
		self.cl_ass = input ("Enter the class: ")

		### Default PBF ##################################################

		self.egress_interface = input ("Enter the egress interface (Or leave empty for none): ")
		self.next_hop = input ("Enter the next hop (Or leave empty for none)": )
		self.symmetric_return = input ("Do you want symmetric return to be enforced (Y/N): ")
		self.schedule = input ("Enter the schedule (Or leave empty for none): ")

	











if int(Policy_Type) == 1:
	print(f"\nset audit-comment xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/security/rules/entry[@name='{PreRulename}'] comment {PreComment}\n")
elif int(Policy_Type) == 2:
	print(f"\nset audit-comment xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/nat/rules/entry[@name='{PreRulename}'] comment {PreComment}\n")
else:
	print(f"\nset audit-comment xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/qos/rules/entry[@name='{PreRulename}'] comment {PreComment}\n")

	# Send_String = (f"\nset audit-comment xpath /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/{Policy_Type}/rules/entry[@name='{Rulename}'] comment {Comment}\n")
