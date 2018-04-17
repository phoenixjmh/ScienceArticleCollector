from django.shortcuts import render
import scraper as SS
import collector as COL







def index(request):
	SS.Scrape()

	context = { 'dictionary':SS.listContainer }

	return render(request, 'index.html', context)


def collect(request):
	COL.main()
	return render(request, 'index.html')
