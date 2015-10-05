#!/usr/bin/env python3
import logging
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

__project__ = 'Kapty'
__version__ = "0.0.1"
__license__ = "CC-BY-SA"

log = logging.getLogger('Kapty')

# Base URL of Website
# BASE_URL = 'https://kat.cr'
BASE_URL = 'http://katproxy.com'
BASE_SCHEME = 'http'
BASE_HOSTNAME = 'katproxy.com'
BASE_SEARCH_URI = '/advanced/'
BASE_VERIFIED = False


# SWITCH (joke) Defaults
# Category DICT for semantic-ish code
class CATEGORY:
	ANY = '0'
	ANIME = 'anime'
	ANIME_MUSIC_VIDEO = 'amv'
	ANIME_ENGLISH = 'english-translated'
	ANIME_OTHER = 'other-anime'
	APPLICATIONS = 'applications'
	WINDOWS = 'windows'
	MAC = 'mac-software'
	UNIX = 'unix'
	LINUX = 'linux'
	IOS = 'ios'
	ANDROID = 'android'
	HANDHELD_APPLICATIONS = 'handheld-applications'
	APPLICATIONS_OTHER = 'other-applications'
	BOOKS = 'books'
	EBOOKS = 'ebooks'
	COMICS = 'comics'
	MAGAZINES = 'magazines'
	TEXTBOOKS = 'textbooks'
	ACADEMIC = 'academic'
	FICTION = 'fiction'
	NONFICTION = 'non-fiction'
	AUDIO_BOOKS = 'audio-books'
	POETRY = 'poetry'
	NEWSPAPER = 'newspapers'
	BOOKS_OTHER = 'other-books'
	GAMES = 'games'
	PC_GAMES = 'pc-games'
	MAC_GAMES = 'mac-games'
	PS2 = 'ps2'
	PS3 = 'ps3'
	PS4 = 'ps4'
	PSP = 'psp'
	PS_VITA = 'ps-vita'
	XBOX_360 = 'xbox360'
	XBOX_ONE = 'xbox-one'
	WII = 'wii'
	NDS = 'nds'
	IOS_GAMES = 'ios-games'
	ANDROID_GAMES = 'android-games'
	HANDHELD_GAMES = 'handheld-games'
	GAMES_OTHER = 'other-games'
	MOVIES = 'movies'
	MOVIES_3D = '3d-movies'
	MOVIES_CLIPS = 'movies-clips'
	MOVIES_HANDHELD = 'handheld_movies'
	MOVIES_IPAD = 'ipad-movies'
	MOVIES_HIGHRES = 'highres-movies'
	MOVIES_ULTRAHD = 'ultrahd'
	MOVIES_BOLLYWOOD = 'bollywood'
	MOVIES_CONCERTS = 'concerts'
	MOVIES_DUBBED = 'dubbed-movies'
	MOVIES_ASIAN = 'asian'
	MOVIES_ANIMATION = 'animation'
	MOVIES_DOCUMENTARY = 'documentary'
	MOVIES_TRAILER = 'trailer'
	MOVIES_OTHER = 'other-movies'
	MUSIC = 'music'
	MUSIC_MP3 = 'mp3'
	MUSIC_AAC = 'aac'
	MUSIC_LOSSLESS = 'lossless'
	MUSIC_TRANSCODE = 'transcode'
	MUSIC_SOUNDTRACK = 'soundtrack'
	MUSIC_RADIO_SHOWS = 'radio-shows'
	MUSIC_KARAOKE = 'karaoke'
	MUSIC_OTHER = 'other-music'
	OTHER = 'other'
	PICTURES = 'pictures'
	SOUND_CLIPS = 'sound-clips'
	COVERS = 'covers'
	WALLPAPERS = 'wallpapers'
	TUTORIALS = 'tutorials'
	SUBTITLES = 'subtitles'
	FONTS = 'fonts'
	UNSORTED = 'unsorted'
	TV = 'tv'
	TV_OTHER = 'other-tv'
	XXX = 'xxx'
	XXX_VIDEO = 'xxx-video'
	XXX_HD_VIDEO = 'xxx-hd-video'
	XXX_ULTRAHD_VIDEO = 'xxx-ultrahd-video'
	XXX_PICTURES = 'xxx-pictures'
	XXX_MAGAZINES = 'xxx-magazines'
	XXX_BOOKS = 'xxx-books'
	XXX_HENTAI = 'hentai'
	XXX_GAMES = 'xxx-games'
	XXX_OTHER = 'other-xxx'


# When Added
class ADDED:
	ANY = 'Any time'
	LAST_HOUR = 'hour'
	LAST_DAY = '24h'
	LAST_WEEK = 'week'
	LAST_MONTH = 'month'
	LAST_YEAR = 'year'


# Language
class LANGUAGE:
	ANY = ''
	ENGLISH = '2'
	ALBANIAN = '42'
	ARABIC = '7'
	BASQUE = '44'
	BENGALI = '46'
	BRAZILIAN = '39'
	BULGARIAN = '37'
	CANTONESE = '45'
	CATALAN = '47'
	CHINESE = '10'
	CROATIAN = '34'
	CZECH = '32'
	DANISH = '26'
	DUTCH = '8'
	FILIPINO = '11'
	FINNISH = '31'
	FRENCH = '5'
	GERMAN = '4'
	GREEK = '30'
	HEBREW = '25'
	HINDI = '6'
	HUNGARIAN = '27'
	ITALIAN = '3'
	JAPANESE = '15'
	KANNADA = '49'
	KOREAN = '16'
	LITHUANIAN = '43'
	MALAYALAM = '21'
	MANDARIN = '23'
	NEPALI = '48'
	NORWEGIAN = '19'
	PERSIAN = '33'
	POLISH = '9'
	PORTUGUESE = '17'
	PUNJABI = '35'
	ROMANIAN = '18'
	RUSSIAN = '12'
	SERBIAN = '28'
	SLOVENIAN = '36'
	SPANISH_LATIN_AMERICA = '41'
	SPANISH_SPAIN = '14'
	SWEDISH = '20'
	TAMIL = '13'
	TELUGU = '22'
	THAI = '24'
	TURKISH = '29'
	UKRAINIAN = '40'
	VIETNAMESE = '38'


# Game Platforms
class PLATFORM:
	ANY = ''
	ANDROID = '4'
	BLACKBERRY = '7'
	GAMECUBE = '15'
	IPAD = '18'
	IPHONE = '19'
	IPOD = '20'
	JAVA = '22'
	LINUX = '24'
	MAC = '25'
	NINTENDO_3DS = '31'
	NINTENDO_DS = '33'
	NUON_DVD = '35'
	OTHER = '65'
	PALM_OS = '37'
	PC = '38'
	PLAYSTATION_2 = '43'
	PLAYSTATION_3 = '44'
	PLAYSTATION_4 = '66'
	PSP = '45'
	SYMBIAN = '52'
	WII = '56'
	WII_U = '68'
	WINDOWS_CE = '57'
	WINDOWS_MOBILE = '58'
	WINDOWS_PHONE = '59'
	XBOX = '61'
	XBOX_360 = '62'
	XBOX_ONE = '67'


def Search():
	return KatSearch()


def RedefineGlobals(url):
	global BASE_URL, BASE_SCHEME, BASE_HOSTNAME
	parts = urlparse(url)
	BASE_URL = '%s://%s' % (parts.scheme, parts.netloc)
	BASE_SCHEME = '%s' % parts.scheme
	BASE_HOSTNAME = '%s' % parts.netloc


class KatSearch(object):
	# String search
	_allWords = []
	_exactWords = []
	_anyWords = []
	_notWords = []

	_category = None
	_user = None

	# About Results
	_whenAdded = None
	_minSeeds = 0
	_numFiles = None

	# TV / Movie
	_imdbId = None
	_tvRangeId = None
	_ISBN = None
	_language = None

	_familySafe = None
	_verifiedOnly = None

	# TV
	_season = None
	_episode = None

	# Games
	_platform = None

	def __init__(self):
		pass

	def find(self, search):
		self._allWords.append(search)
		return self

	def find_exact(self, search):
		self._exactWords.append(search)
		return self

	def find_any(self, search):
		self._anyWords.append(search)
		return self

	def find_without(self, search):
		self._notWords.append(search)
		return self

	def category(self, category):
		self._category = category
		return self

	def user(self, user):
		self._user = user
		return self

	def added(self, added):
		self._whenAdded = added
		return self

	def minimum_seeds(self, number):
		self._minSeeds = number
		return self

	def number_files(self, number):
		self._numFiles = number
		return self

	def imdb_id(self, id):
		self._imdbId = id
		return self

	def tvrange_id(self, id):
		self._tvRangeId = id
		return self

	def isbn(self, id):
		self._ISBN = id
		return self

	def language(self, language):
		self._language = language
		return self

	def family_friendly(self, boolean):
		self._familySafe = boolean
		return self

	def verified_torrents(self, boolean):
		self._verifiedOnly = boolean
		return self

	def tv_season(self, number):
		self._season = number
		return self

	def tv_episode(self, number):
		self._episode = number
		return self

	def platform(self, platform):
		self._platform = platform
		return self

	def run(self):

		global BASE_VERIFIED

		if BASE_VERIFIED is False:
			verify = requests.get(BASE_URL)
			RedefineGlobals(verify.url)
			BASE_VERIFIED = True

		r = requests.Session()

		post = {
			'all': ' '.join(self._allWords),
			'exact': ' '.join(self._exactWords),
			'or': ' '.join(self._anyWords),
			'sub': ' '.join(self._notWords),
			'category': self._category or CATEGORY.ANY,
			'user': self._user,
			'seeds': self._minSeeds,
			'age': self._whenAdded or ADDED.ANY,
			'files': self._numFiles,
			'imdb': self._imdbId,
			'tv': self._tvRangeId,
			'isbn': self._ISBN,
			'lang_sel': self._language or LANGUAGE.ANY,
			'season': self._season,
			'episode': self._episode,
			'platform_id': self._platform or PLATFORM.ANY
		}

		log.debug("Search Start \n{ %s }", ", ".join(['%s: %s \n' % (value, post[value]) for n, value in enumerate(post)]))

		headers = {
			':host': '%s' % BASE_HOSTNAME,
			':method': 'POST',
			':path': '%s' % BASE_SEARCH_URI,
			':scheme': '%s' % BASE_SCHEME,
			':version': 'HTTP/1.1',
			'accept': 'text/html,application/xhtml+xml,application/xml;0.9,image/webp,*/*;q=0.8',
			'accept-encoding': 'gzip, deflate',
			'accept-language': 'en-US,en',
			'cache-control': 'no-cache',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': '%s' % BASE_URL,
			'pragma': 'no-cache',
			'thanks': '%s/' % BASE_URL,
			'upgrade-insecure-requests': 1
		}
		result = r.post("%s%s" % (BASE_URL, BASE_SEARCH_URI), data=post, headers=headers)
		log.debug('Response Code %i' % result.status_code)
		if result.status_code == requests.codes.ok:

			# TODO: Determine if Movie or TV Result

			soup = BeautifulSoup(result.text, 'html.parser')
			print(len(soup.find('table', {'class': 'data'})))
			return KatSearchResult(soup.find('table', {'class': 'data'}), post)

		elif result.status_code == '404':
			return KatSearchResult([], post)


class KatBaseResult:
	_query = None
	_raw = None
	_results = []
	_total = 0
	_page = 1

	def __init__(self, raw, query):
		self._raw = raw
		self._query = query


class KatSearchResult(KatBaseResult):
	pass


class KatTVResult(KatBaseResult):
	pass


class KatMovieResult(KatBaseResult):
	pass
