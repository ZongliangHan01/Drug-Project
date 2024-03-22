import csv
import pandas as pd
data = """
No.,Drug Name,Active Ingredient,Date,FDA-approved use on approval date*
45,Zurampic,lesinurad,12/22/2015,To treat high blood uric acid levels associated with gout
44,Uptravi,selexipag,12/21/2015,To treat pulmonary arterial hypertension
43,Bridion,sugammadex,12/15/2015,To reverse effects of neuromuscular blocking drugs used during surgery
42,Alecensa,alectinib,12/11/2015,To treat ALK-positive lung cancer
41,Kanuma,sebelipase alfa,12/8/2015,To treat patients with a rare disease known as lysosomal acid lipase (LAL) deficiency
40,Empliciti,elotuzumab,11/30/2015,To treat people with multiple myeloma who have received one to three prior medications
39,Portrazza,necitumumab,11/24/2015,To treat patients with advanced (metastatic) squamous non-small cell lung cancer (NSCLC) who have not previously received medication specifically for treating their advanced lung cancer
38,Ninlaro,ixazomib,11/20/2015,To treat people with multiple myeloma who have received at least one prior therapy
37,Darzalex,daratumumab,11/16/2015,To treat patients with multiple myeloma who have received at least three prior treatments.
36,Tagrisso,osimertinib,11/13/2015,To treat certain patients with non-small cell lung cancer
35,Cotellic,cobimetinib,11/10/2015,To be used in combination with vemurafenib to treat advanced melanoma that has spread to other parts of the body or can’t be removed by surgery, and that has a certain type of abnormal gene (BRAF V600E or V600K mutation)
34,Genvoya,a fixed-dose combination tablet containing elvitegravir, cobicistat, emtricitabine, and tenofovir alafenamide,11/5/2015,For use as a complete regimen for the treatment of HIV-1 infection in adults and pediatric patients 12 years of age and older
33,Nucala,mepolizumab,11/4/2015,For use with other asthma medicines for the maintenance treatment of asthma in patients age 12 years and older.
32,Strensiq,asfotase alfa,10/23/2015,To treat perinatal, infantile and juvenile-onset hypophosphatasia (HPP).
31,Yondelis,trabectedin,10/23/2015,To treat specific soft tissue sarcomas (STS) – liposarcoma and leiomyosarcoma – that cannot be removed by surgery (unresectable) or is advanced (metastatic).
30,Veltassa,patiromer for oral suspension,10/21/2015,To treat hyperkalemia, a serious condition in which the amount of potassium in the blood is too high.
29,Praxbind,idarucizumab,10/16/2015,For use in patients who are taking the anticoagulant Pradaxa (dabigatran) during emergency situations when there is a need to reverse Pradaxa’s blood-thinning effects.
28,Aristada,aripiprazole lauroxil,10/5/2015,To treat adults with schizophrenia
27,Tresiba,insulin degludec injection,9/25/2015,To improve blood sugar (glucose) control in adults with diabetes mellitus
26,Lonsurf,trifluridine and tipiracil,9/22/2015,To treat patients with an advanced form of colorectal cancer who are no longer responding to other therapies
25,Vraylar,cariprazine,9/17/2015,To treat schizophrenia and bipolar disorder in adults
24,Xuriden,uridine triacetate,9/4/2015,To treat patients with hereditary orotic aciduria
23,Varubi,rolapitant,9/1/2015,To prevent delayed phase chemotherapy-induced nausea and vomiting (emesis)
22,Repatha,evolocumab,8/27/2015,To treat certain patients with high cholesterol
21,Addyi,flibanserin,8/18/2015,To treat acquired, generalized hypoactive sexual desire disorder (HSDD) in premenopausal women
20,Daklinza,daclatasvir,7/24/2015,To treat chronic hepatitis C virus (HCV) genotype 3 infections
19,Odomzo,sonidegib,7/24/2015,To treat patients with locally advanced basal cell carcinoma that has recurred following surgery or radiation therapy, or who are not candidates for surgery or radiation therapy.
18,Praluent,alirocumab,7/24/2015,To treat certain patients with high cholesterol
17,Rexulti,brexpiprazole,7/10/2015,To treat schizophrenia and as an add on to an antidepressant to treat major depressive disorder
16,Entresto,sacubitril/valsartan,7/7/2015,To treat heart failure
15,Orkambi,lumacaftor 200 mg/ivacaftor 125 mg,7/2/2015,To treat cystic fibrosis
14,Kengreal,cangrelor,6/22/2015,To prevent the formation of harmful blood clots in the coronary arteries for adult patients undergoing percutaneous coronary intervention
13,Viberzi,eluxadoline,5/27/2015,To treat irritable bowel syndrome with diarrhea (IBS-D) in adult men and women.
12,Kybella,deoxycholic acid,4/29/2015,To treat adults with moderate-to-severe fat below the chin, known as submental fat
11,Corlanor,ivabradine,4/15/2015,To reduce hospitalization from worsening heart failure.
10,Cholbam,cholic acid,3/17/2015,To treat pediatric and adult patients with bile acid synthesis disorders due to single enzyme defects, and for patients with peroxisomal disorders
9,Unituxin,dinutuximab,3/10/2015,To treat pediatric patients with high-risk neuroblastoma
8,Cresemba,capsule injection isavuconazonium sulfate,3/6/2015,To treat adults with invasive aspergillosis and invasive mucormycosis, rare but serious infections
7,Avycaz,ceftazidime-avibactam,2/25/2015,To treat adults with complicated intra-abdominal infections (cIAI), in combination with metronidazole, and complicated urinary tract infections (cUTI), including kidney infections (pyelonephritis), who have limited or no alternative treatment options.
6,Farydak,panobinostat,2/23/2015,To treat patients with multiple myeloma
5,Lenvima,lenvatinib,2/13/2015,To treat patients with progressive, differentiated thyroid cancer (DTC) whose disease progressed despite receiving radioactive iodine therapy (radioactive iodine refractory disease).
4,Ibrance,palbociclib,2/3/2015,To treat advanced (metastatic) breast cancer
3,Natpara,parathyroid hormone,1/23/2015,To control hypocalcemia (low blood calcium levels) in patients with hypoparathyroidism
2,Cosentyx,secukinumab,1/21/2015,To treat adults with moderate-to-severe plaque psoriasis
1,Savaysa,edoxaban,1/8/2015,To reduce the risk of stroke and dangerous blood clots (systemic embolism) in patients with atrial fibrillation that is not caused by a heart valve problem
"""

# Split data into lines and parse each line into a dictionary
rows = [line.split(',') for line in data.strip().split('\n')]

# Write data to a CSV file
with open('FDA_drug_approvals.csv', 'w', newline='') as csvfile:
    fieldnames = rows[0]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in rows[1:]:
        writer.writerow({fieldnames[i]: row[i] for i in range(len(fieldnames))})

df = pd.read_csv('FDA_drug_approvals.csv')
df.to_excel('FDA_drug_approvals.xlsx', index=False)