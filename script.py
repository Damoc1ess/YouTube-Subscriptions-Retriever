import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Définir la portée : ici, lecture seule de tes données YouTube
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def parse_date(date_str):
    """Parse une date ISO 8601 avec ou sans microsecondes."""
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

def main():
    # Authentification via OAuth 2.0
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json',
        SCOPES
    )
    credentials = flow.run_local_server(port=0)
    
    # Construction du service YouTube
    youtube = build('youtube', 'v3', credentials=credentials)
    
    subscriptions = []
    nextPageToken = None

    # Récupération de tous les abonnements (pagination)
    while True:
        request = youtube.subscriptions().list(
            part='snippet',
            mine=True,
            maxResults=50,
            pageToken=nextPageToken
        )
        response = request.execute()
        subscriptions.extend(response.get('items', []))
        nextPageToken = response.get('nextPageToken')
        if not nextPageToken:
            break

    # Tri des abonnements du plus vieux au plus récent en se basant sur 'publishedAt'
    subscriptions = sorted(subscriptions, key=lambda sub: parse_date(sub['snippet']['publishedAt']))

    # Préparer le contenu à écrire dans le fichier
    output_lines = []
    output_lines.append("Liste de tes abonnements (du plus vieux au plus récent) avec la date d'abonnement et le nombre de jours depuis l'abonnement :\n")
    for sub in subscriptions:
        title = sub['snippet']['title']
        # Date d'abonnement au format ISO 8601
        subscribed_at = sub['snippet']['publishedAt']

        subscribed_date = parse_date(subscribed_at)

        # Calcul du nombre de jours depuis l'abonnement
        days_since = (datetime.datetime.utcnow() - subscribed_date).days
        
        output_lines.append(f"Chaîne : {title}")
        output_lines.append(f"Abonné(e) depuis le : {subscribed_date.strftime('%Y-%m-%d')} ({days_since} jours)")
        output_lines.append("-" * 40)

    # Écriture du résultat dans un fichier texte
    with open("subscriptions.txt", "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

    print("Les résultats ont été écrits dans le fichier subscriptions.txt")

if __name__ == '__main__':
    main()
