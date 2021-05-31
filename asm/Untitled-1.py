
         Assets=Asset.objects.all()
    assetfilter=ReportFilter(request.GET, queryset=Assets)
    Assets=assetfilter.qs
    context= {'Assets':Assets,'assetfilter':assetfilter, }
    return render(request, 'asm/report.html',context)
        
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-=Disposition']='attachment; filename=Asset_Report' +\
        str(datetime.datetime.now())+'csv'


    writer= csv.writer(response)
    writer.writerow(['AssetName', 'Description','RegionalOffice', 'Status', 'DatePurch', 'DisposalDate'])
    Assets=Asset.objects.all()
    assetfilter=ReportFilter(request.GET, queryset=Assets)
    assets=assetfilter.qs


    for asset in assets :
        writer.writerow([asset.AssetName, asset.Description,asset.RegionalOffice, asset.Status, asset.DatePurch, asset.DisposalDate])
    return response
#def export_pdf(request):
   # pass