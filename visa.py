from pyknow import *

class VisaProcessing(KnowledgeEngine):

    @DefFacts()
    def requirements(self):
        yield Fact(action="get_visa_or_not")

    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Genuine Passport"))
    def genuine_passport(self):
       global satisfy_requirements
       satisfy_requirements +=10


    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Valid Passport exceeding six months"))
    def valid_passport(self):
       global satisfy_requirements
       satisfy_requirements +=10

    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Stamped employer cover letter"))
    def stamped_cover_letter(self):
       global satisfy_requirements
       satisfy_requirements +=10

    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Certified bank statement"))
    def bank_statement(self):
       global satisfy_requirements
       satisfy_requirements +=10

    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Passport photos"))
    def passport_photos(self):
       global satisfy_requirements
       satisfy_requirements +=10

    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Application form completed"))
    def completed_application(self):
       global satisfy_requirements
       satisfy_requirements +=10

    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Return air ticket"))
    def return_air_ticket(self):
       global satisfy_requirements
       satisfy_requirements +=10

    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Hotel booking confirmation"))
    def hotel_confirmation(self):
       global satisfy_requirements
       satisfy_requirements +=10

    @Rule(Fact(action='get_visa_or_not'),
          Fact(requirement="Is person has someone known in the destination country"))
    def yf_card(self):
       global satisfy_requirements
       satisfy_requirements +=10

    @Rule(Fact(action='get_visa_or_not'),
          OR(Fact(requirement="Previous application approved"),
             Fact(requirement="Previous visa not overstayed"),
             Fact(requirement="Entry to Canada not denied")))
    def previous_visa_approved(self):
       global satisfy_requirements
       satisfy_requirements +=3.3

          
satisfy_requirements =0
missing_document=""
print("")
print(" Canada embassy visa expert. ".center(70, "*"))
print(" Note ".center(70, "*"))
print (" Answer through y (yes) or n (no) ".center(70, "*"))
print ("Type (Done) to stop and show the results ".center(70, "*"))
print(" ")

engine = VisaProcessing()


reqrmts = open("requirements.txt")
reqrmts_t = reqrmts.read()
requirements_list = reqrmts_t.split("\n")
reqrmts.close()
  
print("Has the visa applicant satisfied these visa requirements? ( type yes/y or no/n)")
print("\n")
for item in requirements_list:
    print(str(requirements_list.index(item)+1) + ". " + item)
    # Uncomment the line below to show the scores as you progress to fill the questions. 

    requirement = input()

    #  If any of the first nine mandatory requirements are missing, the system breaks and outputs the document is missing.
    if requirements_list.index(item) < 9 and (requirement.strip().lower() == "no" or requirement.strip().lower() == "n"):
      missing_document = item
      break

    if requirement.strip().lower() == "Done":
      break
    if (requirement.strip().lower() == "yes" or requirement.strip().lower() == "y"):
      engine.reset()  # Prepare the engine for the execution.
      engine.declare(Fact(requirement=item))
      engine.run()


# Print the results.
print("")
print(" Result. ".center(40, "*")) 
print("score is: ")  
print(satisfy_requirements)   
if (satisfy_requirements < 90):
    print("All application must have at least the first 9 requirements satisfied. We are sorry the applicant does not satisfy to get the visa.")
    if missing_document != "":
      print("")
      print(missing_document + " is missing in this application hence visa cannot be given.")
elif (satisfy_requirements > 93) :
    print ("The applicant can be granted the visa")
elif ((satisfy_requirements >= 90 ) and (satisfy_requirements <= 93)):
    print ("The applicant MAY be granted the visa but first review with Consular officer")
print(" Result. ".center(40, "*"))
print("")
