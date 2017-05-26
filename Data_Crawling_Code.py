# -*- coding: utf-8 -*-
import requests

#import csv
from bs4 import BeautifulSoup

url = r"C:\Users\kshit\Desktop\test.html"
page = open(url)
i = 0
li_counter = 0
soup = BeautifulSoup(page.read())
initial_accused_list = []
for tag in soup.findAll('li'):
    li_counter = li_counter + 1
    # Skipping the unwanted records
    if (li_counter>6):
# Append the records into list
        initial_accused_list.append(tag.find('a')['href'])
        # Taking the first 100 Records
    if(li_counter==106):
        break
header = ['First_name', 'Last_name', 'Sex', 'Age','Place_of_residence_settlement','Place_of_residence_parish', 'Place_of_residence_presbytery',\
'Place_of_residence_county', 'Place_of_residence_burgh', 'Marital_status', 'Socioeconomic_status', 'Notes_list', 'Acc_family_name',\
'Acc_family_Title','Acc_Family_Relationship', 'Acc_Family_Age', 'Acc_family_occupation', 'Start_date', 'End_date' ,'Characterisation', 'Notes_on_characterisation',\
'Notes_on_case','People_desig_notes','Trial_info', 'Reference','Q_Info_non_natural_being_notes','Q_info_Apperance_NN_type_being','Q_info_Demonic_pact_and_notes',\
'Q_info_witches_meeting','Q_info_withch_meeting_place_and_loc','Q_info_folk_c_Specific_ver_for ','Q_info_folk_c_Specific_rti_facts','Q_info_folk_Sympathetic_magic',\
'Q_info_folk_notes','Q_info_counter_strategies','Q_info_shape_change_types_and_notes','Q_info_ritual_objs','Q_info_disease_ill_Human_illness','Q_info_disease_ill_Human_death',\
'Q_info_disease_ill_Animal_illness','Q_info_disease_ill_Healing_animals','Q_info_disease_ill_Animal_death','Q_info_disease_ill_Transferring_disease','Q_info_disease_ill_Laying_on','Q_info_disease_ill_Quarrelling',\
'Q_info_disease_ill_Cursing','Q_info_disease_ill_Recognised_healer','Q_info_disease_ill_Healing_humans','Q_info_disease_ill_Notes','Q_info_cause_witch_malice','Q_info_other_malice_property_damage',\
'Q_info_other_malice_Weather_mod','Q_info_other_malice_Notes','Q_info_property_damage','Q_info_Weather_modification','Q_info_other_charges']
with open("E:\Rise Spring 2017\Advance Business Intelligence\Project\Data_Set_Data_World.txt", "a") as text_file:
    header = str(header) + ("\n")
    header = header.replace("[","").replace("]","").replace("'","")
    text_file.write(header)
    
    for k in initial_accused_list:
        First_name = []
        Last_name = []
        sex_list = []
        place_of_residence_parish = []
        place_of_residence_presbytery = []
        place_of_residence_county = []
        Place_of_residence_burgh = []
        Marital_status = []
        Socioeconomic_status = []
        age_list = []
        notes_list = []
        Occupation = []
        Relationship = []
        name = []
        title = []
        Place_of_residence_settlement = []
        r = requests.get(k)
        soup = BeautifulSoup(r.content)
        for tag in soup.findAll('th'):
            a = tag.parent
            for m in a.findAll('th'):
                an = (m.string)
    
    
                        
            for n in a.findAll('td'):
                if (an == "First Name"):
                    First_name.append(n.string)
                elif (an == "Last Name"):
                    Last_name.append(n.string)
                elif(an == "Sex" ):
                    sex_list.append(n.string)
                elif(an =="Place of residence - parish" ):
                    place_of_residence_parish.append(n.string)
                elif(an == "Place of residence - presbytery"):
                    place_of_residence_presbytery.append(n.string)
                elif(an == "Place of residence - county"):
                    place_of_residence_county.append(n.string)
                elif(an=="Place of residence - burgh"):
                    Place_of_residence_burgh.append(n.string)
                elif(an == "Socioeconomic status"):
                    Socioeconomic_status.append(n.string)
                elif(an == "Age"):
                    age_list.append(n.string)
                elif(an == "Marital status"):
                    Marital_status.append(n.string)
                elif(an == "Notes"):
                    notes_list.append(n.string)
                elif(an=="Relationship"):
                    Relationship.append(n.string)
                elif(an == "Place of residence - settlement"):
                    Place_of_residence_settlement.append(n.string)
        
        acc_fam_name = ""
        acc_fam_Title = ""
        acc_fam_Relationship = ""
        acc_fam_Age = ""
        acc_fam_occ =""
        for tag in soup.findAll('table')[1].findAll('table')[1].find_all('h2'):
            if (tag.string == "Accused's family"):
                acc_fam= []
                for tag in soup.findAll('table')[1].findAll('table')[2].find_all('th'):
                    print(tag.string)
                for t  in soup.findAll('table')[1].findAll('table')[2].find_all('td'):
                    a = str(t.string)
                    a = a.strip()
                    acc_fam.append(a)
                if(acc_fam[0] != None):
                    acc_fam_name = str(acc_fam[0]).replace(","," ")
                if(acc_fam[1] != None):
                    acc_fam_Title = str(acc_fam[1]).replace(","," ")
                if(acc_fam[2] != None):
                    acc_fam_Relationship = str(acc_fam[2]).replace(","," ")
                if(acc_fam[3] != None):
                    acc_fam_Age = str(acc_fam[3]).replace(","," ")
                if(acc_fam[4] != None):
                    acc_fam_occ = str(acc_fam[4]).replace(","," ")
                    
        age_list = str(age_list)
        age_list = age_list[1:4].replace("'","")
        
        for tag in soup.findAll('table')[1].findAll('table')[-1].find_all(('a')):
            # Case involving accused URL
            Case_url_raw = (tag['href'])
        Casre_url = "http://webdb.ucs.ed.ac.uk/witches/"+ Case_url_raw
        
        # Case Details
        Start_date = []
        End_date = []
        Characterisation = []
        Notes_on_characterisation = []
        Notes_on_case = []
            
        r = requests.get(Casre_url)
        soup = BeautifulSoup(r.content)
        cnt = 0
        cnp = 0
        for tag in soup.findAll('table')[1].findAll('table')[0].find_all('th'):
            for asd in tag.parent.findAll('th'):
                cnt = cnt + 1
                if (cnt == 1):
                    continue
                else:
                    #case_detail_title.append(asd.string)
                    ani = asd.string
                    #print(ani)
                        
            for asw in tag.parent.findAll('td'):
                cnp=cnp+1
                if(cnp == 1):
                    continue
                else:
                    if (ani == 'Start date'):
                        Start_date.append(asw.string)
                    elif(ani == 'End date'):
                        End_date.append(asw.string)
                    elif(ani == 'Characterisation'):
                        qws = (asw.get_text())
                        qws = qws.strip()
                        Characterisation.append(qws.replace(",",""))
                    elif(ani == 'Notes on characterisation'):
                        Notes_on_characterisation.append(asw.string.replace(",",""))
                    elif(ani == 'Notes on case'):
                        Notes_on_case.append(asw.string.replace(",",""))
                        
                        
        ## people involved in case
        r = requests.get(Casre_url)
        people_involved_title = []
            
        counter = 0;
        people_desig_notes = ""
        soup = BeautifulSoup(r.content)
        for tag in soup.findAll('table')[1].findAll('table')[1].find_all('td'):
                if (counter == 0):
                    people_involved_title.append(tag.string)
                else:
                   #print(tag.string)
                    if(tag.string == None):
                        people_desig_notes=people_desig_notes+" NA "+";"
                    else:
                        people_desig_notes = (people_desig_notes+(tag.string)+ ";")
                counter = counter + 1
        people_desig_notes.replace(",", " ")     
        # Trial Details
        r = requests.get(Casre_url)
        people_involved_title = []
        trial_info = ""
        soup = BeautifulSoup(r.content)
        iteration = 0
        
        if (len(people_desig_notes) > 5):
            for tag in soup.findAll('table')[1].findAll('table')[2].find_all('a'):
                #iteration = iteration + 1
                if (iteration == 1):
                    
                    continue
                else:
                    mnc = tag.get_text()
                    mnc = mnc.strip()
                    mnc = mnc.replace(","," ")
                    trial_info = (trial_info + mnc + "; ")
                iteration = iteration + 1
        else:
            for tag in soup.findAll('table')[1].findAll('table')[1].find_all('a'):
                
                if (iteration == 1):
                    continue
                else:
                    mnc = tag.get_text()
                    mnc = mnc.strip()
                    mnc = mnc.replace(","," ")
                    trial_info = (trial_info + mnc + "; ")
                iteration = iteration + 1
        Reference = ""
        h_cnt = 0
        for tag in soup.findAll('table')[1].findAll('table')[-1].find_all('td'):
            h_cnt = h_cnt + 1
            if(h_cnt == 1):
                continue
                #print(tag.get_text())
            else:
                abc = tag.get_text()
                abc = abc.strip()
                abc = abc.replace(","," ")
                Reference = (Reference + abc + "; ")
        Q_Info_non_natural_being_notes = ""
        
        Q_info_Apperance_NN_type_being = ""
        
        Q_info_Demonic_pact_and_notes = ""
        
        Q_info_witches_meeting = ""
        
        Q_info_withch_meeting_place_and_loc = ""
        
        Q_info_folk_c_Specific_ver_for = ""
        
        Q_info_folk_c_Specific_rti_facts = ""
        
        Q_info_folk_Sympathetic_magic = ""
        
        Q_info_folk_notes = ""
        
        Q_info_counter_strategies = ""
        
        Q_info_shape_change_types_and_notes = ""
        
        Q_info_ritual_objs =""
        
        Q_info_disease_ill_Human_illness =""
        Q_info_disease_ill_Human_death =""
        Q_info_disease_ill_Animal_illness =""
        Q_info_disease_ill_Animal_death=""
        Q_info_disease_ill_Healing_animals=""
        Q_info_disease_ill_Transferring_disease=""
        Q_info_disease_ill_Laying_on=""
        Q_info_disease_ill_Quarrelling=""
        Q_info_disease_ill_Cursing=""
        Q_info_disease_ill_Recognised_healer=""
        Q_info_disease_ill_Healing_humans=""
        Q_info_disease_ill_Notes=""
        
        Q_info_cause_witch_malice =""
        
        Q_info_other_malice_property_damage =""
        
        Q_info_other_malice_Weather_mod =""
        
        Q_info_other_malice_Notes =""
        
        Q_info_property_damage =""
        
        Q_info_Weather_modification =""
        
        Q_info_other_charges =""
        
        # Non-natural beings
        for w in range(1,21):
            try:
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Non-natural beings"):
                        for t in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            Q_Info_non_natural_being_notes = t.string
                
            except IndexError:
                pass
        print(Q_Info_non_natural_being_notes)  
        
        # Appearance of Non-natural beings
        for w in range(1,21):
            try:
                cntm = 0           
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Appearance of Non-natural beings"):
                        for m in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                avm = str(m.string)
                                if(avm != None):
                                    Q_info_Apperance_NN_type_being = Q_info_Apperance_NN_type_being + avm + " ^ "
            except IndexError:
                pass               
                    
        print(Q_info_Apperance_NN_type_being)
        print(cntm)
        #Demonic pact
        for w in range(1,21):
            try:
                cntm = 0
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Demonic pact"):
                        for g in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            var = g.string
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                adp = str(g.string)
                                Q_info_Demonic_pact_and_notes = Q_info_Demonic_pact_and_notes + adp + " ^ "
            except IndexError:
                pass                         
        #Witches' Meetings
        for w in range(1,21):
            try:
                cntm = 0
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Witches' Meetings"):
                        for p in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            agh = p.parent.get_text()
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var3 = str(p.parent.get_text())
                                var3 = var3.replace("Y", " Y").replace("N", " N")
                                Q_info_witches_meeting = Q_info_witches_meeting + var3 + " ^ "
            except IndexError:
                pass  
            
        # Witches' Meeting Place
        for w in range(1,21):
            try:
                cntm = 0
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Witches' Meeting Place"):
                        for z in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            #print(z.get_text())
                            aghz = z.get_text()
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var4 = str(z.get_text())
                                
                                Q_info_withch_meeting_place_and_loc = Q_info_withch_meeting_place_and_loc + var4 + " ^ "
            except IndexError:
                pass                  
        print(Q_info_withch_meeting_place_and_loc)
        #Folk Culture  
        for w in range(1,21):
            try:
                cntm = 0
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Folk Culture"):
                        for y in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            #print(y.parent.get_text())
                            op =y.parent.get_text()
                            if (op[:10] == "Specific v"):
                                Q_info_folk_c_Specific_ver_for = op[24:27]
                            if (op[:10] == "Specific r"):
                                Q_info_folk_c_Specific_rti_facts = op[20:24]
                            if(op[:10] == "Sympatheti"):
                                Q_info_folk_Sympathetic_magic =op[17:21]
                            if(op[:10] == "Folk Notes"):
                                Q_info_folk_notes = op[10:]
                                Q_info_folk_notes = ("\"") + Q_info_folk_notes +("\"")
        
            except IndexError:
                pass                    
        print(Q_info_folk_c_Specific_ver_for)
        print(Q_info_folk_c_Specific_rti_facts)
        print(Q_info_folk_Sympathetic_magic)
        print(Q_info_folk_notes)
                    
        #<h3>Counter strategies</h3>
        for w in range(1,21):
            try:
                cntm = 0
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Counter strategies"):
                        for r1 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var5 = str(r1.get_text())
                                Q_info_counter_strategies = Q_info_counter_strategies + var5 + " ^ "
            except IndexError:
                pass                           
        print(Q_info_counter_strategies)
        
        #Shape-changing
        for w in range(1,21):
            try:
                cntm = 0
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Shape-changing"):
                        for r2 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var6 = str(r2.get_text())
                                Q_info_shape_change_types_and_notes = Q_info_shape_change_types_and_notes + var6 + " ^ "
            except IndexError:
                pass                           
        print(Q_info_shape_change_types_and_notes)
        #Q_info_ritual_objs   
        for w in range(1,21):
            try:             
                cntm = 0
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Ritual objects"):
                        for r3 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var7 = str(r3.get_text())
                                Q_info_ritual_objs = Q_info_ritual_objs + var7 + " ^ "
            except IndexError:
                pass   
        #print(Q_info_ritual_objs)
        
        #Diseases/Illness
        for w in range(1,21):
            try:   
                cntm = 0
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Diseases/Illness"):
                        for r4 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                op2 = r4.parent.get_text()
                                if (op2[:13] == "Human illness"):
                                    Q_info_disease_ill_Human_illness= op2[13:16]
                                if (op2[:11] == "Human death"):
                                    Q_info_disease_ill_Human_death = op2[11:14]
                                if(op2[:14] == "Animal illness"):
                                    Q_info_disease_ill_Animal_illness =op2[14:17]
                                if(op2[:15]=="Healing animals"):
                                    Q_info_disease_ill_Healing_animals = op2[15:18]
                                if(op2[:12]== "Animal death"):
                                    Q_info_disease_ill_Animal_death =op2[12:15]
                                if(op2[:20] == "Transferring disease"):
                                    Q_info_disease_ill_Transferring_disease =op2[20:23]
                                if(op2[:9] == "Laying on"):
                                    Q_info_disease_ill_Laying_on =op2[9:12]
                                if(op2[:11] == "Quarrelling"):
                                    Q_info_disease_ill_Quarrelling =op2[11:14]
                                if(op2[:7] == "Cursing"):
                                    Q_info_disease_ill_Cursing =op2[7:10]
                                if(op2[:17] == "Recognised healers"):
                                    Q_info_disease_ill_Recognised_healer =op2[17:20]
                                if(op2[:14] == "Healing humans"):
                                    Q_info_disease_ill_Healing_humans =op2[14:17]
                                if(op2[:16] == "Notes on disease"):
                                    Q_info_disease_ill_Notes =op2[16:]
                                    Q_info_disease_ill_Notes = ("\"") + Q_info_disease_ill_Notes +("\"")
            except IndexError:
                pass   
                        
                    
        #Cause of witch's malice   
        for w in range(1,21):
            try:  
                cntm = 0         
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Cause of witch's malice"):
                        for r5 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var9 = str(r5.get_text())
                                Q_info_cause_witch_malice = Q_info_cause_witch_malice + var9 + " ^ "
            except IndexError:
                pass                           
        print(Q_info_cause_witch_malice)
        
        #Other maleficia 14
        Q_info_other_malice_property_damage =""
        
        Q_info_other_malice_Weather_mod =""
        
        Q_info_other_malice_Notes =""
        for w in range(1,21):
            try: 
                cntm = 0         
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Other maleficia"):
                        for r6 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                               # print(r6.parent.get_text())
                                op1 =r6.parent.get_text()
                                if (op1[:15] == "Property damage"):
                                    Q_info_other_malice_property_damage= op1[15:20]
                                if (op1[:20] == "Weather modification"):
                                    Q_info_other_malice_Weather_mod = op1[20:24]
                                if(op1[:5] == "Notes"):
                                    Q_info_other_malice_Notes =op1[5:]
                                    Q_info_other_malice_Notes = ("\"") + Q_info_other_malice_Notes +("\"")
            except IndexError:
                pass       
        
        #Property damage
        for w in range(1,21):
            try: 
                cntm = 0         
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Property damage"):
                        for r7 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var11 = str(r7.get_text())
                                Q_info_property_damage = Q_info_property_damage + var11 + " ^ "
            except IndexError:
                pass       
                                
        print(Q_info_property_damage)
                
        #Weather modification
        for w in range(1,21):
            try: 
                cntm = 0         
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Weather modification"):
                        for r8 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var12 = str(r8.get_text())
                                Q_info_Weather_modification = Q_info_Weather_modification + var12 + " ^ "
            except IndexError:
                pass                          
        print(Q_info_Weather_modification)
                        
        #Other charges
        for w in range(1,21):
            try:                 
                cntm = 0         
                for tag in soup.findAll('table')[1].findAll('table')[w].find_all('h3'):
                    if (tag.string == "Other charges"):
                        for r9 in soup.findAll('table')[1].findAll('table')[w].find_all('td'):
                            #print(r9.get_text())
                            cntm = cntm + 1
                            if (cntm == 1):
                                continue
                            else:
                                var13 = str(r9.get_text())
                                Q_info_other_charges  = Q_info_other_charges  + var13 + " ^ "    
            except IndexError:
                pass                           
        print(Q_info_other_charges)  
                
                
                
                               
        
        title_list_a = " "
        notes_list = str(notes_list).replace(",","")
        title_list_a =  (str(First_name) +"," + str(Last_name) +"," + str(sex_list) +"," + (age_list) + "," +str(Place_of_residence_settlement) + "," + str(place_of_residence_parish) +"," + str(place_of_residence_presbytery)+"," +\
                        str(place_of_residence_county)+"," +str(Place_of_residence_burgh)+"," + str(Marital_status) + "," + str(Socioeconomic_status)+ "," + (notes_list)+ "," +\
                        acc_fam_name +"," + acc_fam_Title +"," + acc_fam_Relationship +"," + acc_fam_Age +"," + acc_fam_occ +"," +\
                        str(Start_date)+ ", " + \
                        str(End_date) + "," + str(Characterisation) + "," + str(Notes_on_characterisation) +"," +  str(Notes_on_case) + "," + people_desig_notes + "," + trial_info + "," + Reference + "," +\
                        Q_Info_non_natural_being_notes + "," + Q_info_Apperance_NN_type_being + "," + Q_info_Demonic_pact_and_notes + "," +\
                        Q_info_witches_meeting + "," + Q_info_withch_meeting_place_and_loc + "," + Q_info_folk_c_Specific_ver_for + "," +\
                        Q_info_folk_c_Specific_rti_facts + "," + Q_info_folk_Sympathetic_magic + "," +  Q_info_folk_notes + "," +\
                        Q_info_counter_strategies + "," +  Q_info_shape_change_types_and_notes + "," +  Q_info_ritual_objs + "," +\
                        Q_info_disease_ill_Human_illness + "," +  Q_info_disease_ill_Human_death + "," + Q_info_disease_ill_Animal_illness + "," +\
                        Q_info_disease_ill_Healing_animals+ "," + Q_info_disease_ill_Animal_death + "," + Q_info_disease_ill_Transferring_disease + "," +  Q_info_disease_ill_Laying_on + "," +\
                        Q_info_disease_ill_Quarrelling + "," + Q_info_disease_ill_Cursing + "," +  Q_info_disease_ill_Recognised_healer + "," +\
                        Q_info_disease_ill_Healing_humans + "," +  Q_info_disease_ill_Notes + "," +  Q_info_cause_witch_malice + "," +\
                        Q_info_other_malice_property_damage + "," +  Q_info_other_malice_Weather_mod + "," +  Q_info_other_malice_Notes + "," +\
                        Q_info_property_damage + "," +  Q_info_Weather_modification + "," + Q_info_other_charges + "," +"\n")
                        
    
        
        title_list_a = title_list_a.replace("[", "").replace("]","").replace("'"," ")
        
        text_file.write(title_list_a)
        


    