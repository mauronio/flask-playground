import cx:Oracle

OER_ASSETS_SQL = """ 
	SELECT A.id, A.name AssetName, nvl(A.version, '0'), A.description, nvl(AT.name, 'tipo desconocido') AssetTypeName, AT.id AssetTypeID,  CA.name FunctionName,
               nvl(substr(A.name, 2, instr(A.name, '}', 1, 1)-2), '(Sin  Dominio)') DomainName, 
               nvl(substr(A.name, 
               	instr(A.name, '}', 1, 1) + 1, 
               	instr(A.name, '/', -1, 1) - (instr(A.name, '}', 1, 1)+1)), '(Sin Contexto)') ContextName,
               substr(A.name, instr(A.name, '/', -1, 1) + 1) SimpleName

	 FROM SOAOER.ASSETS A, SOAOER.ASSETTYPES AT, SOAOER.ASSETCATEGORIZATIONS AC, SOAOER.CATEGORIZATIONS CA  
	 where A.AssetTypeID = AT.id 
	  and A.id = AC.assetid  
	  and AC.catid = CA.id 
	  and CA.superid = 50352 
	  and AT.Id = 50204 -- Service Type
	  order by 7, 9, 10
	"""

def get_oer_assets():
    con = cx_Oracle.connect('mgomez/mgomez@oer.vtr.cl/orcl')
    cur = con.cursor()
    cur.prepare(OER_ASSETS_SQL)
    cur.execute(None)

    results_columns = { 
        'assetID': 'ID', 
        'assetName': 'Nombre de Servicio', 
        'assetType': 'ID Tipo de Servicio', 
        'assetTypeName': 'Nombre de Tipo de Servicio', 
        'assetFunctionname': 'Funcion del Servicio'
    }

    results_rows = []

    for row in cur:

        # Encabezado Asset
        assetID = row[0]
        assetRawName = row[1]
        assetDomainName = row[7]
        assetContextName = row[8]
        assetShortName = row[9]  + ' v' + row[2] + ' (' + row[4] + ')'
        assetName = assetSimpleName + ' v' + row[2] + ' (' + row[4] + ')'
        assetType = row[5]
        assetTypeName = row[4]
        assetFunctionName = row[6]

        result_rows.append({
            'assetID': 'ID',
            'assetName': 'Nombre de Servicio',
            'assetType': 'ID Tipo de Servicio',
            'assetTypeName': 'Nombre de Tipo de Servicio',
            'assetFunctionname': 'Funcion del Servicio'
        })
    
    results = {
        'columns': results_columns
        'rows': results_rows
    }

    cur.close()
    con.close()

    return results




