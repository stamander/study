import json
import datetime
from dateutil.relativedelta import relativedelta  #日付に月単位で加算減産する

targetAccounts = {{targetAccounts}}
accountQuery='''select id,CONCAT("ftra",LPAD(id,4,0)) as aid ,name from ftra.account where id in(%s) order by id'''% (targetAccounts)
accounts = execute_query('forte_ftra_readonly', accountQuery)['rows']


for account in accounts:
    query = ''' use %s;
SELECT
	period.month,
	period.siteId AS siteId,
	site.name as siteName,
	sumCalls,
	sumClicks,
	sumCloses,
	ctc,
	vtc,
	sumSessions,
	sumPvs
FROM
	(
		SELECT
			DATE_FORMAT(visitDate,"%%Y-%%m-01") AS MONTH,
			visitDate,
			siteId,
			SUM(calls) AS sumCalls,
			SUM(clicks) AS sumClicks,
			SUM(closes) AS sumCloses,
			CASE WHEN browserName in ("Amazon Silk","BlackBerry WebKit","BlackBerry","CFNetwork","Chrome Mobile WebView","Chrome Mobile iOS","Chrome Mobile","DuckDuckGo Mobile","Edge Mobile","Facebook Messenger","Facebook","FacebookBot","Firefox Mobile","Firefox iOS","IE Mobile","Kurio App","MicroB","Mint Browser","MiuiBrowser","Mobile Safari UI/WKWebView","Mobile Safari","Nokia Browser","Nokia OSS Browser","Nokia Services (WAP) Browser","ONE Browser","Opera Coast","Opera Mini","Opera Mobile","Ovi Browser","Palm Blazer","Palm Pre","Polaris","QQ Browser Mini","QQ Browser Mobile","QQ Browser","Samsung Internet","TopBuzz","UC Browser") THEN "SP" ELSE "PC" END AS deviceType
		from
			cta_report_period
		WHERE 
			visitDate BETWEEN '%s' AND '%s'
		GROUP BY MONTH,siteId
	) period
LEFT JOIN 
    site ON period.siteId= site.id
LEFT JOIN
    (
		select
			DATE_FORMAT(visitDate,"%%Y-%%m-01") AS MONTH,
			SUM(pvs) AS sumPvs,
        	SUM(sessions) AS sumSessions,
        	siteId
        from
            cta_report_summary
		WHERE 
			visitDate BETWEEN '%s' AND '%s'
        group by MONTH,siteId
    ) summary ON
        period.month = summary.month AND
        period.siteId = summary.siteId
LEFT JOIN
	(
		select
			DATE_FORMAT(visitDate,"%%Y-%%m-01") AS MONTH,
			SUM(ctc) AS ctc,
			SUM(vtc) AS vtc,
			siteId
		from
			cta_report_summary_cv
		WHERE 
			visitDate BETWEEN '%s' AND '%s'
		GROUP BY 
			MONTH,siteId
	) cv ON 
		period.month = cv.month AND
		period.siteId = cv.siteId

GROUP BY MONTH,siteId order by month asc''' %(account["aid"],"{{ term.start }}","{{ term.end }}","{{ term.start }}","{{ term.end }}","{{ term.start }}","{{ term.end }}");
    reports = execute_query('forte_ftra_readonly', query)['rows']
    for report in reports:
        add_result_row(result,{
          "年月":report["month"],
          "accountId": account["aid"],
          "siteId":report["siteId"],
          "オファー発動数":report["sumCalls"],
          "クリック数":report["sumClicks"],
          "クローズ数":report["sumCloses"],
          "account_id":account["id"],
          "アカウント名":account["name"],
          "サイト名":report["siteName"],
          "CTC":report["ctc"],
          "VTC":report["vtc"],
          "セッション":report["sumSessions"],
          "PV":report["sumPvs"]
        })
        
add_result_column(result, '年月', '', 'string')
add_result_column(result, 'siteId', '', 'integer')
add_result_column(result, 'オファー発動数', '', 'integer')
add_result_column(result, 'クリック数', '', 'integer')
add_result_column(result, 'クローズ数', '', 'integer')
add_result_column(result, 'サイト名', '', 'string')
add_result_column(result, 'account_id', '', 'string')
add_result_column(result, 'アカウント名', '', 'string')
add_result_column(result, 'CTC', '', 'integer')
add_result_column(result, 'VTC', '', 'integer')
add_result_column(result, 'セッション', '', 'integer')
add_result_column(result, 'PV', '', 'integer')
