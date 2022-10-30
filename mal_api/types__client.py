from __future__ import annotations
from typing import Optional
from typing import Union

MangaRankingType = Union[
    "all",
    "manga",
    "oneshots",
    "doujin",
    "lightnovels",
    "novels",
    "manhwa",
    "manhua",
    "bypopularity",
    "favorite",
]

MangaStatus = Union[
    "reading",
    "completed",
    "on_hold",
    "dropped",
    "plan_to_read",
]

MangaSortVaildValues = Union[
    "list_score",
    "list_updated_at",
    "manga_title",
    "manga_start_date",
]

AnimeStatus = Union[
    "watching",
    "completed",
    "on_hold",
    "dropped",
    "plan_to_watch",
]

AnimeRankType = Union[
    "all",
    "airing",
    "upcoming",
    "tv",
    "ova",
    "movie",
    "special",
    "bypopularity",
    "favorite",
]

UserAnimeSortVaildValues = Union[
    "list_score",
    "list_updated_at",
    "anime_title",
    "anime_start_date",
]
AnimeSeasonSort = Union[
    "anime_score", "anime_num_list_users",
]

AnimeSeason = Union[
    "winter", "spring", "summer", "fall",
]


class AnimeDataNodeMainPicture:
    medium: str  # JPEG URL
    large: str  # JPEG URL


class AnimeDataNode:
    id: int
    title: str
    main_picture: AnimeDataNodeMainPicture


class AnimeDataListStatus:
    finish_date: Optional[str]  # datetime
    start_date: Optional[str]  # datetime

    status: str
    score: int
    num_episodes_watched: int
    is_rewatching: bool
    updated_at: str  # datetime


class AnimeData:
    node: AnimeDataNode
    list_status: AnimeDataListStatus


class Paging:
    next: Optional[str]  # url
    previous: Optional[str]  # url


class UserAnimeList:
    data: list[AnimeData]
    paging: Paging


class UserAnimeStatistics:
    mean_score: float
    num_days: float
    num_days_completed: float
    num_days_dropped: float
    num_days_on_hold: float
    num_days_watched: float
    num_days_watching: float
    num_episodes: int
    num_items: int
    num_items_completed: int
    num_items_dropped: int
    num_items_on_hold: int
    num_items_plan_to_watch: int
    num_items_watching: int
    num_times_rewatched: int


class UserData:
    id: int
    name: str
    location: str
    joined_at: str
    birthday: str  # Date
    anime_statistics: UserAnimeStatistics
