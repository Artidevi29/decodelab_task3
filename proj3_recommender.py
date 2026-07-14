"""
Project 3: AI Recommendation Logic
------------------------------------
Goal: recommend items to a user based on their stated preferences.

Approach: a lightweight content-based recommender. Each movie is tagged
with a set of genres. The user picks genres they're interested in, and
we score every movie by how much its genre set overlaps with the user's
picks (Jaccard similarity -- intersection over union). This is the same
basic idea real recommendation engines use before things get fancy with
collaborative filtering or embeddings: represent items as feature sets,
represent the user's taste the same way, then measure similarity.

Run it with: python proj3_recommender.py
"""

import random

# A small hand-built catalog is enough to demonstrate the logic clearly.
# In a real system this would come from a database or an API instead.
MOVIE_CATALOG = [
    {"title": "Galactic Drift",        "genres": {"sci-fi", "action", "adventure"}},
    {"title": "The Last Recipe",       "genres": {"drama", "romance"}},
    {"title": "Silent Alarm",          "genres": {"thriller", "mystery"}},
    {"title": "Two Left Feet",         "genres": {"comedy", "romance"}},
    {"title": "Iron Horizon",          "genres": {"sci-fi", "action"}},
    {"title": "Whispers in the Attic", "genres": {"horror", "mystery"}},
    {"title": "The Long Way Home",     "genres": {"drama", "adventure"}},
    {"title": "Punchline",             "genres": {"comedy"}},
    {"title": "Deep Cover",            "genres": {"thriller", "action"}},
    {"title": "Orbit Zero",            "genres": {"sci-fi", "drama"}},
    {"title": "Late Night Laughs",     "genres": {"comedy", "drama"}},
    {"title": "The Hollow Path",       "genres": {"horror", "thriller"}},
]

ALL_GENRES = sorted({genre for movie in MOVIE_CATALOG for genre in movie["genres"]})


def jaccard_similarity(set_a, set_b):
    """
    Intersection over union. Returns 0.0 if there's no overlap and no
    way to compute a ratio (both sets empty), and up to 1.0 for a
    perfect match.
    """
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union


def get_user_preferences():
    """
    Ask the user which genres they like. Accepts a comma-separated list
    and validates against the known genre list so a typo doesn't just
    silently fail to match anything later.
    """
    print("Available genres:", ", ".join(ALL_GENRES))
    raw = input("Which genres are you in the mood for? (comma-separated): ")

    chosen = {g.strip().lower() for g in raw.split(",") if g.strip()}
    valid = chosen & set(ALL_GENRES)
    invalid = chosen - set(ALL_GENRES)

    if invalid:
        print(f"(Ignoring unrecognized genres: {', '.join(invalid)})")

    return valid


def recommend(preferences, catalog=MOVIE_CATALOG, top_n=5):
    """
    Score every movie against the user's preference set, then return the
    top N by score. Ties are broken randomly rather than by catalog
    order, so the same preferences don't always surface movies in the
    same order every run -- closer to how a real recommender would avoid
    always pushing the same "first" result.
    """
    scored = []
    for movie in catalog:
        score = jaccard_similarity(preferences, movie["genres"])
        if score > 0:
            scored.append((movie["title"], movie["genres"], score))

    random.shuffle(scored)  # break ties randomly before the stable sort
    scored.sort(key=lambda item: item[2], reverse=True)

    return scored[:top_n]


def display_recommendations(preferences, results):
    if not preferences:
        print("\nNo valid genres selected -- can't build recommendations from nothing.")
        return

    print(f"\nBased on your interest in: {', '.join(sorted(preferences))}")

    if not results:
        print("No matching movies found. Try a different genre combination.")
        return

    print("Here's what I'd recommend:\n")
    for rank, (title, genres, score) in enumerate(results, start=1):
        print(f"{rank}. {title:<20} (match: {score:.0%}) -- genres: {', '.join(sorted(genres))}")


def run_demo_case():
    """
    A non-interactive demo pass so the logic can be sanity-checked
    without needing to type anything -- useful for quickly verifying the
    scoring behaves sensibly before wiring up the interactive version.
    """
    print("=== Demo run (no input required) ===")
    demo_preferences = {"sci-fi", "action"}
    results = recommend(demo_preferences)
    display_recommendations(demo_preferences, results)
    print()


if __name__ == "__main__":
    run_demo_case()

    print("=== Interactive mode ===")
    user_preferences = get_user_preferences()
    recommendations = recommend(user_preferences)
    display_recommendations(user_preferences, recommendations)
