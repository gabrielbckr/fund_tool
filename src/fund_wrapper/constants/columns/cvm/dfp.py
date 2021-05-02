class DFP:
    DOC_DATE = 'ReferenceDate'
    MONETARY_SCALE = 'ESCALA_MOEDA'
    ACCOUNT = 'AccountID'
    ACCOUNT_VALUE = 'AccountValue'
    CNPJ = 'CNPJ'
    DATE = 'Date'
    CO_NAME = 'CompanyName'
    CO_CVM_ID = 'CVM_ID'
    ACCOUNT_DESCRIPTION = 'AccountDescription'


DFP_RENAME = {
    'CNPJ_CIA': DFP.CNPJ,
    'DT_REFER': DFP.DATE,
    # 'VERSAO': ,
    'DENOM_CIA': DFP.CO_NAME,
    'CD_CVM': DFP.CO_CVM_ID,
    # 'GRUPO_DFP',
    # 'MOEDA': DFP.CURRENCY,
    #'ORDEM_EXERC': ,
    # 'DT_FIM_EXERC': DFP.DATE,
    'CD_CONTA': DFP.ACCOUNT,
    'DS_CONTA': DFP.ACCOUNT_DESCRIPTION,
    'VL_CONTA': DFP.ACCOUNT_VALUE,
    #'ST_CONTA_FIXA'
}
