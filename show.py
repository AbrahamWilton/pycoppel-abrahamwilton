class Show:
    def __init__(self, show_data):
        self.id = show_data.get("id")
        self.url = show_data.get("url")
        self.name = show_data.get("name")
        self.type = show_data.get("type")
        self.language = show_data.get("language")
        self.genres = show_data.get("genres", [])
        self.status = show_data.get("status")
        self.runtime = show_data.get("runtime")
        self.average_runtime = show_data.get("averageRuntime")
        self.premiered = show_data.get("premiered")
        self.ended = show_data.get("ended")
        self.official_site = show_data.get("officialSite")
        
        self.schedule = show_data.get("schedule", {})
        self.schedule_time = self.schedule.get("time")
        self.schedule_days = self.schedule.get("days", [])

        self.rating = show_data.get("rating", {})
        self.average_rating = self.rating.get("average")

        self.weight = show_data.get("weight")

        self.network = show_data.get("network", {})
        self.network_id = self.network.get("id")
        self.network_name = self.network.get("name")

        self.country = self.network.get("country", {})
        self.country_name = self.country.get("name")
        self.country_code = self.country.get("code")
        self.country_timezone = self.country.get("timezone")

        self.network_official_site = self.network.get("officialSite")

        self.web_channel = show_data.get("webChannel")
        self.dvd_country = show_data.get("dvdCountry")

        self.externals = show_data.get("externals", {})
        self.tvrage = self.externals.get("tvrage")
        self.thetvdb = self.externals.get("thetvdb")
        self.imdb = self.externals.get("imdb")

        self.image = show_data.get("image", {})
        self.image_medium = self.image.get("medium")
        self.image_original = self.image.get("original")

        self.summary = show_data.get("summary")

        self.updated = show_data.get("updated")

        self.links = show_data.get("_links", {})
        self.self_link = self.links.get("self", {}).get("href")
        self.previousepisode_link = self.links.get("previousepisode", {}).get("href")
