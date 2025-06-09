# -*- coding: utf-8 -*-
"""

Internal Audit Automated Testing

Search & Highlight Test Samples in a PDF

"""


#----------IMPORTS
import pandas as pd
import fitz             #Package pyMuPDF

#----------Variables, file and evidence_paths

sample_number = 1

evidence_path = r"PATH/TO/EVIDENCE/PDF"
test_data = r"PATH/TO/TEST/DATA"
sample_path = 'PATH/TO/SAMPLE/FOLDER'


#----------Extract data from test_data

samples = pd.read_excel(test_data, 
                        sheet_name='Sample Testing',      #Pick Excel sheet
                        skiprows=2,                       #Ignore first two rows
                        index_col=0)                      #Use column 0 for index

#---------- Get Search Data from samples

amount = samples.transaction_amount[sample_number]
dater = samples.transaction_date[sample_number]

#----------Search in Doc
try:
    doc = fitz.open(evidence_path)                   # Open Evidence PDF
    pages = list(range(doc.page_count))              # Gets list of pages
    amount = "{:,.2f}".format(amount)                # format amount for search
    amount = " " + amount + " "                      # add spaces
    date_text = "{:%#m/%#d/%Y}".format(dater)        # format date for search
    
    del_list = []                                    #List of pages to delete
    page_list = []                                   #List of pages
    date_list = []                                   #List of dates

    
    for pg in pages:                                 #For Loop
        page = doc[pg]                               #Pick page to search
        amount_instances = page.search_for(amount)   #Search for amount
        date_instances = page.search_for(date_text)  #Search for date
        
        # match corresponding date (this section selects same row using position)
        for ai in amount_instances:                  
            ai_1, ai_3 = ai[1]+.0005, ai[3]+.0005
            for di in date_instances:
                di_1, di_3 = di[1]+.0005, di[3]+.0005
                if di_1 <= ai_1 and di_3 >= ai_3:
                    pass
                else:
                    date_instances.remove(di)
                    
        if len(amount_instances)!=0 and len(date_instances)!=0:   #Did we find a match?
            page_list.append(pg)                                  #Add good page
            date_list.append(pg)                                  
        else:
            del_list.append(pg)                                   #Page to be deleted
            
        ### HIGHLIGHT
        for inst in amount_instances:
            highlight = page.add_highlight_annot(inst)            #Highlight amount
            
    del_list.sort(reverse=True)                                   #Sort del list
             
    for pg in del_list:                                           #Delete all
        doc.delete_page(pg)                                       #unecessary pages
    
        
    #---- Save sample file
    
    filename = "SAMPLE -"+str(sample_number)+" pg "+str(page_list[0]+1)  #create sample filename
    
    doc.save(sample_path+filename+".pdf", 
             garbage=4, deflate=True, clean=True)                  #Save sample

    print(f'Sample {sample_number} - Pass')                      #Indicate pass
                              

except:
    print(f'Sample {sample_number} - FAIL')                      #Indicate Fail
    pass

    
