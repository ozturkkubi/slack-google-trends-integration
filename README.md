# slack-google-trends-integration

# Trending Keywords Slack Notifier

This repository contains a Python script that retrieves trending keywords from Google using the Google Trends API and sends them to a specified Slack channel. It allows you to stay updated on the latest search trends for different countries.

## Features

- Retrieves trending search keywords from Google Trends for specified countries.
- Connects to the Slack API to send the trending keywords to a designated Slack channel.
- Provides an organized and formatted message with the trending keywords for each country.

## Prerequisites

To run the script, you need to have the following:

- Python 3.x installed on your machine.
- Required Python packages: pandas, pytrends, requests.

## Installation

1. Clone this repository to your local machine using the following command:

git clone https://github.com/ozturkkubi/slack-google-trends-integration/


2. Install the necessary Python packages by running the following command:


## Usage

1. Obtain a Slack API token by creating a new Slack app and generating an API token with the required permissions.

2. Update the `SLACK_API_TOKEN` variable in the code with your Slack API token.

3. Set the `SLACK_CHANNEL_NAME` variable to the name of the Slack channel where you want to send the trending keywords.

4. Customize the list of countries in the `countries` variable to retrieve trending keywords for specific countries.

5. Run the script using the following command:


The script will fetch the trending keywords from Google Trends and send them to the specified Slack channel.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

This script utilizes the following libraries:

- pandas: [https://pandas.pydata.org/](https://pandas.pydata.org/)
- pytrends: [https://pypi.org/project/pytrends/](https://pypi.org/project/pytrends/)
- requests: [https://pypi.org/project/requests/](https://pypi.org/project/requests/)

Special thanks to the developers of these libraries for their contributions.


