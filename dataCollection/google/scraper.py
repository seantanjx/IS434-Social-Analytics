from googlemaps import GoogleMapsScraper
from datetime import datetime, timedelta
import argparse
import csv
from pymongo import MongoClient
import ssl

HEADER = ['id_review', 'caption', 'relative_date', 'retrieval_date', 'rating', 'username', 'n_review_user', 'n_photo_user', 'url_user']
HEADER_W_SOURCE = ['id_review', 'caption', 'relative_date','retrieval_date', 'rating', 'username', 'n_review_user', 'n_photo_user', 'url_user', 'url_source']

db = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

def csv_writer(source_field, path='', outfile='gm_reviews.csv'):
    targetfile = open(path + outfile, mode='w', encoding='utf-8', newline='\n')
    writer = csv.writer(targetfile, quoting=csv.QUOTE_MINIMAL)

    if source_field:
        h = HEADER_W_SOURCE
    else:
        h = HEADER
    writer.writerow(h)

    return writer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Google Maps reviews scraper.')
    parser.add_argument('--N', type=int, default=100, help='Number of reviews to scrape')
    parser.add_argument('--i', type=str, default='urls.txt', help='target URLs file')
    parser.add_argument('--place', dest='place', action='store_true', help='Scrape place metadata')
    parser.add_argument('--debug', dest='debug', action='store_true', help='Run scraper using browser graphical interface')
    parser.add_argument('--source', dest='source', action='store_true', help='Add source url to CSV file (for multiple urls in a single file)')
    parser.set_defaults(place=False, debug=False, source=False)

    args = parser.parse_args()

    # store reviews in CSV file
    writer = csv_writer(args.source)
    
    ##########################################################
    #Change the DB path when running the script
    ##########################################################

    
    db_name = db.googlereviews.googlefreshfruitlab
    with GoogleMapsScraper(debug=args.debug) as scraper:
        with open(args.i, 'r') as urls_file:
            for url in urls_file:

                if args.place:
                    print(scraper.get_account(url))
                else:
                    error = scraper.sort_by_date(url)
                    if error == 0:

                        n = 0
                        while n < args.N:
                            reviews = scraper.get_reviews(n)

                            for r in reviews:
                                row_data = list(r.values())
                               
                                item = {
                                    'id': row_data[0],
                                    'review': row_data[1],
                                    'caption': row_data[2],
                                    'date': row_data[3],
                                    'rating': row_data[4],
                                    'user': row_data[6]

                                }

                                result_status = db_name.insert_one(item)

                                if args.source:
                                    row_data.append(url)

                                writer.writerow(row_data)

                            n += len(reviews)