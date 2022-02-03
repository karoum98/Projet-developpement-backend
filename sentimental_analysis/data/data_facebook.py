from apify_client import ApifyClient

def data_from_facebook(filiales, dateDebut):
    data = {
        "Maroc" : [],
        "Mauritanie" : [],
        "Sénégal" : [],
        "Burkina Faso" : [],
        "Bénin" : [],
        "Togo" : [],
        "Ghana" : [],
        "Kenya" : [],
        "Mozanbique" : [],
        "Cameroun" : [],
        "Côte d'ivoire" : [],
        "Guinée" : [],
        "Tchad" : [],
        "Congo" : [],
        "Madagascar" : []
    }

    # Initialize the ApifyClient with your API token
    client = ApifyClient("apify_api_bVtADrfiMTX4GOjKkNNQQQe5nsPrXU3F89b1")

    # Prepare the actor input
    run_input = {
        "startUrls": [
            {
                "url": "https://www.facebook.com/societegenerale.senegal"
            },
            {
                "url": "https://www.facebook.com/SocGenTchad"
            },
            {
                "url": "https://www.facebook.com/Guinee.SocieteGenerale"
            },
            {
                "url": "https://www.facebook.com/Soci%C3%A9t%C3%A9-g%C3%A9n%C3%A9rale-du-Cameroun-106128635174834"
            },
            {
                "url": "https://www.facebook.com/societegenerale.congo"
            },
            {
                "url": "https://www.facebook.com/societegenerale.france"
            }
        ]
    }

    # Run the actor and wait for it to finish
    run = client.actor("pocesar/facebook-latest-comments-scraper").call(run_input=run_input)

    # Fetch and print actor results from the run's dataset (if there are any)
    for filiale in filiales:
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            if list(item.keys())[0] != "#error":
                for comment in item['comments']:
                    data[filiale].append([ comment['text'], item['postUrl'], comment['authorId'] ])

    return data