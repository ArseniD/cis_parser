import csv
import json

from argparse import ArgumentParser


def load_data(data):
    with open(data) as f:
        data = json.load(f)
    return data


def write_csv(json_data):
    f = csv.writer(open("cis_output.csv", "w"))
    # Create headers
    f.writerow(["country", "country_name", "store_name", "external_id"])
    for data in json_data:
        f.writerow([data["address"]["country"],
                    data["address"]["country_name"],
                    data["store_name"],
                    data["external_id"],
                    ])


def create_parser():
    parser = ArgumentParser(description="""
    Parse json data based on file and write necessary fields in a CSV file.""")
    parser.add_argument('--path', '-p',
                        required=True,
                        help="the path to the json file")
    return parser


if __name__ == '__main__':
    args = create_parser().parse_args()

    try:
        if args.path:
            data = load_data(args.path)
            write_csv(data)
    except IOError as error:
        print(error)
