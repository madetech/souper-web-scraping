from models.report import ReportOut

VALID_REPORTS = [
    ReportOut(
        id=1748,
        assessment_date='2023-06-14',
        overall_verdict='Met',
        name='request-a-standard-or-enhanced-dbs-check',
        url='/service-standard-reports/request-a-standard-or-enhanced-dbs-check',
        stage='Alpha reassessment',
        service_provider='HMRC'),
    ReportOut(
        id=1749,
        assessment_date='2022-11-29',
        overall_verdict='Met',
        name='apply-for-a-voter-authority-certificate-beta-assessment',
        url='/service-standard-reports/apply-for-a-voter-authority-certificate-beta-assessment',
        stage='Beta',
        service_provider='HMRC')
]