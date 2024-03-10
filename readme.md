## Ecolab - NER - CSP


### How to run?

```
conda create -n ner39 -y python=3.9

conda activate ner39

python ner.py
```


### Standardize
```

```


### Run Testcases:
```
Address-Pattern-NER-20240305
https://syndigo-my.sharepoint.com/:x:/r/personal/raja_raman_syndigo_com/_layouts/15/Doc.aspx?sourcedoc=%7BCDB645B0-52D6-4F4F-AFC7-05E5FC4F50F4%7D&file=Book%203.xlsx&action=editnew&mobileredirect=true&wdNewAndOpenCt=1709620017905&ct=1709620018676&wdOrigin=OFFICECOM-WEB.START.NEW&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=0813768f-0739-4594-9c90-bd985f876144&login_hint=Raja.Raman%40syndigo.com&cid=d108cf7f-9401-4860-8ce8-484ffce80609

download file and put it into
~/datasets/Address-Pattern-NER-20240305-3.xlsx

python predict_local.py
```


### How to run FastAPI?
```
uvicorn fast:app --reload
```


### How to make inputs?
```
for CoreNLP:





```




### Address-CNER-Riversand
https://docs.google.com/spreadsheets/d/1QH_T6C3MAJNj5f_1gL1dZtLRUjFbwJ4wcHpPwlCfylI/

### Address - Patterns - Raja - Google Sheet:
https://docs.google.com/spreadsheets/d/1RuTw-ycDOy2EUHf0qDp3kVvoZ0_s-bjd4eeRAyZndRk/

### Updated
Match Result_Iteration 2_ReRun_2023 (Ecolab feedback) 11-30-23
https://docs.google.com/spreadsheets/d/14PMNufXfsWASB52py88fGtMnqO8EYnTh_t8ep5drIWc/


### Generate Address
[Generate Address](https://chat.openai.com/share/dcb468e2-904d-45f8-85e8-2371a3f20505)




Pending:
```
1. training inputs has a lot of repetitive entries. We need to find and remove them

```

## How to test?
```
python predict_local.py
```