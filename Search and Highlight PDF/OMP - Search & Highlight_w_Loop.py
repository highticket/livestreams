# -*- coding: utf-8 -*-
"""

Internal Audit Automated Testing

Search & Highlight Test Samples in a PDF

"""


#----------IMPORTS
import pandas as pd
import fitz             #Package pyMuPDF

#----------Variables, file and evidence_paths

#sample_number = 1       Remove the sample_number variable

evidence_path = r"PATH/TO/EVIDENCE/PDF"
test_data = r"PATH/TO/EXCEL/TEST/DATA"
sample_path = 'PATH/TO/EVIDENCE'


#----------Extract data from test_data

samples = pd.read_excel(test_data, 
                        sheet_name='Sample Testing',
                        skiprows=2,
                        index_col=0)

#---------- Get Search Data from samples

for sample_number in samples.index:                    # Add this line for loop
                                                         # indent everything
                                                         # below one time.
    amount = samples.transaction_amount[sample_number]
    dater = samples.transaction_date[sample_number]
    
    
    #----------Search in Doc
    try:
        doc = fitz.open(evidence_path)
        pages = list(range(doc.page_count))
        amount = "{:,.2f}".format(amount)
        amount = " " + amount + " "
        date_text = "{:%#m/%#d/%Y}".format(dater)
        
        del_list = []
        page_list = []
        date_list = []
    
        
        for pg in pages:
            page = doc[pg]
            amount_instances = page.search_for(amount)
            date_instances = page.search_for(date_text)
            
            # match corresponding date
            for ai in amount_instances:
                ai_1, ai_3 = ai[1]+.0005, ai[3]+.0005
                for di in date_instances:
                    di_1, di_3 = di[1]+.0005, di[3]+.0005
                    if di_1 <= ai_1 and di_3 >= ai_3:
                        pass
                    else:
                        date_instances.remove(di)
                        
            if len(amount_instances)!=0 and len(date_instances)!=0:
                page_list.append(pg)
                date_list.append(pg)
            else:
                del_list.append(pg)
                
            ### HIGHLIGHT
            for inst in amount_instances:
                highlight = page.add_highlight_annot(inst)
                
        del_list.sort(reverse=True)
              
        
        for pg in del_list:
            doc.delete_page(pg)
        
            
        #---- Save sample file
        
        filename = "SAMPLE -"+str(sample_number)+" pg "+str(page_list[0]+1)
        
        doc.save(sample_path+filename+".pdf", 
                 garbage=4, deflate=True, clean=True)
    
        print(f'Sample {sample_number} - Pass')               
                                  
    
    except:
        print(f'Sample {sample_number} - FAIL')
        pass

    
