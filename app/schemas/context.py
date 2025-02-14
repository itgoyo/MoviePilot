from pathlib import Path
from typing import Optional, Dict, List, Union

from pydantic import BaseModel

from app.schemas.types import MediaType, NotificationType, MessageChannel


class MetaInfo(BaseModel):
    """
    识别元数据
    """
    # 是否处理的文件
    isfile: Optional[bool] = False
    # 原字符串
    org_string: Optional[str] = None
    # 原标题
    title: Optional[str] = None
    # 副标题
    subtitle: Optional[str] = None
    # 类型 电影、电视剧
    type: Optional[str] = None
    # 名称
    name: Optional[str] = None
    # 识别的中文名
    cn_name: Optional[str] = None
    # 识别的英文名
    en_name: Optional[str] = None
    # 年份
    year: Optional[str] = None
    # 总季数
    total_seasons: Optional[int] = 0
    # 识别的开始季 数字
    begin_season: Optional[int] = None
    # 识别的结束季 数字
    end_season: Optional[int] = None
    # 总集数
    total_episodes: Optional[int] = 0
    # 识别的开始集
    begin_episode: Optional[int] = None
    # 识别的结束集
    end_episode: Optional[int] = None
    # SxxExx
    season_episode: Optional[str] = None
    # Partx Cd Dvd Disk Disc
    part: Optional[str] = None
    # 识别的资源类型
    resource_type: Optional[str] = None
    # 识别的效果
    resource_effect: Optional[str] = None
    # 识别的分辨率
    resource_pix: Optional[str] = None
    # 识别的制作组/字幕组
    resource_team: Optional[str] = None
    # 视频编码
    video_encode: Optional[str] = None
    # 音频编码
    audio_encode: Optional[str] = None
    # 资源类型
    edition: Optional[str] = None
    # 应用的识别词信息
    apply_words: Optional[List[str]] = None


class MediaInfo(BaseModel):
    """
    识别媒体信息
    """
    # 类型 电影、电视剧
    type: Optional[str] = None
    # 媒体标题
    title: Optional[str] = None
    # 年份
    year: Optional[str] = None
    # 标题（年份）
    title_year: Optional[str] = None
    # 季
    season: Optional[int] = None
    # TMDB ID
    tmdb_id: Optional[int] = None
    # IMDB ID
    imdb_id: Optional[str] = None
    # TVDB ID
    tvdb_id: Optional[str] = None
    # 豆瓣ID
    douban_id: Optional[str] = None
    # 媒体原语种
    original_language: Optional[str] = None
    # 媒体原发行标题
    original_title: Optional[str] = None
    # 媒体发行日期
    release_date: Optional[str] = None
    # 背景图片
    backdrop_path: Optional[str] = None
    # 海报图片
    poster_path: Optional[str] = None
    # 评分
    vote_average: Optional[int] = 0
    # 描述
    overview: Optional[str] = None
    # 二级分类
    category: Optional[str] = ""
    # 季季集清单
    seasons: Optional[Dict[int, list]] = {}
    # 季详情
    season_info: Optional[List[dict]] = []
    # 别名和译名
    names: Optional[list] = []
    # 演员
    actors: Optional[list] = []
    # 导演
    directors: Optional[list] = []
    # 详情链接
    detail_link: Optional[str] = None
    # 其它TMDB属性
    adult: Optional[bool] = False
    created_by: Optional[list] = []
    episode_run_time: Optional[list] = []
    genres: Optional[list] = []
    first_air_date: Optional[str] = None
    homepage: Optional[str] = None
    languages: Optional[list] = []
    last_air_date: Optional[str] = None
    networks: Optional[list] = []
    number_of_episodes: Optional[int] = 0
    number_of_seasons: Optional[int] = 0
    origin_country: Optional[list] = []
    original_name: Optional[str] = None
    production_companies: Optional[list] = []
    production_countries: Optional[list] = []
    spoken_languages: Optional[list] = []
    status: Optional[str] = None
    tagline: Optional[str] = None
    vote_count: Optional[int] = 0
    popularity: Optional[int] = 0
    runtime: Optional[int] = None
    next_episode_to_air: Optional[str] = None


class TorrentInfo(BaseModel):
    """
    搜索种子信息
    """
    # 站点ID
    site: Optional[int] = None
    # 站点名称
    site_name: Optional[str] = None
    # 站点Cookie
    site_cookie: Optional[str] = None
    # 站点UA
    site_ua: Optional[str] = None
    # 站点是否使用代理
    site_proxy: Optional[bool] = False
    # 站点优先级
    site_order: Optional[int] = 0
    # 种子名称
    title: Optional[str] = None
    # 种子副标题
    description: Optional[str] = None
    # IMDB ID
    imdbid: Optional[str] = None
    # 种子链接
    enclosure: Optional[str] = None
    # 详情页面
    page_url: Optional[str] = None
    # 种子大小
    size: Optional[float] = 0
    # 做种者
    seeders: Optional[int] = 0
    # 下载者
    peers: Optional[int] = 0
    # 完成者
    grabs: Optional[int] = 0
    # 发布时间
    pubdate: Optional[str] = None
    # 已过时间
    date_elapsed: Optional[str] = None
    # 上传因子
    uploadvolumefactor: Optional[float] = None
    # 下载因子
    downloadvolumefactor: Optional[float] = None
    # HR
    hit_and_run: Optional[bool] = False
    # 种子标签
    labels: Optional[list] = []
    # 种子优先级
    pri_order: Optional[int] = 0
    # 促销
    volume_factor: Optional[str] = None


class Context(BaseModel):
    """
    上下文
    """
    # 元数据
    meta_info: Optional[MetaInfo] = None
    # 媒体信息
    media_info: Optional[MediaInfo] = None
    # 种子信息
    torrent_info: Optional[TorrentInfo] = None


class TransferTorrent(BaseModel):
    """
    待转移任务信息
    """
    title: Optional[str] = None
    path: Optional[Path] = None
    hash: Optional[str] = None
    tags: Optional[str] = None


class DownloadingTorrent(BaseModel):
    """
    下载中任务信息
    """
    hash: Optional[str] = None
    title: Optional[str] = None
    name: Optional[str] = None
    year: Optional[str] = None
    season_episode: Optional[str] = None
    size: Optional[float] = 0
    progress: Optional[float] = 0
    state: Optional[str] = 'downloading'
    upspeed: Optional[str] = None
    dlspeed: Optional[str] = None
    media: Optional[dict] = {}


class TransferInfo(BaseModel):
    """
    文件转移结果信息
    """
    # 转移⼁路径
    path: Optional[Path] = None
    # 转移后路径
    target_path: Optional[Path] = None
    # 处理文件数
    file_count: Optional[int] = 0
    # 总文件大小
    total_size: Optional[float] = 0
    # 失败清单
    fail_list: Optional[list] = []
    # 错误信息
    message: Optional[str] = None


class ExistMediaInfo(BaseModel):
    """
    媒体服务器存在媒体信息
    """
    # 类型 电影、电视剧
    type: Optional[MediaType]
    # 季
    seasons: Optional[Dict[int, list]] = {}


class NotExistMediaInfo(BaseModel):
    """
    媒体服务器不存在媒体信息
    """
    # 季
    season: Optional[int] = None
    # 剧集列表
    episodes: Optional[list] = []
    # 总集数
    total_episodes: Optional[int] = 0
    # 开始集
    start_episode: Optional[int] = 0


class RefreshMediaItem(BaseModel):
    """
    媒体库刷新信息
    """
    # 标题
    title: Optional[str] = None
    # 年份
    year: Optional[str] = None
    # 类型
    type: Optional[MediaType] = None
    # 类别
    category: Optional[str] = None
    # 目录
    target_path: Optional[Path] = None


class TmdbSeason(BaseModel):
    """
    TMDB季信息
    """
    air_date: Optional[str] = None
    episode_count: Optional[int] = None
    name: Optional[str] = None
    overview: Optional[str] = None
    poster_path: Optional[str] = None
    season_number: Optional[int] = None
    vote_average: Optional[float] = None


class TmdbEpisode(BaseModel):
    """
    TMDB集信息
    """
    air_date: Optional[str] = None
    episode_number: Optional[int] = None
    name: Optional[str] = None
    overview: Optional[str] = None
    runtime: Optional[int] = None
    season_number: Optional[int] = None
    still_path: Optional[str] = None
    vote_average: Optional[float] = None
    crew: Optional[list] = []
    guest_stars: Optional[list] = []


class Notification(BaseModel):
    """
    消息
    """
    # 消息渠道
    channel: Optional[MessageChannel] = None
    # 消息类型
    mtype: Optional[NotificationType] = None
    # 标题
    title: Optional[str] = None
    # 文本内容
    text: Optional[str] = None
    # 图片
    image: Optional[str] = None
    # 链接
    link: Optional[str] = None
    # 用户ID
    userid: Optional[Union[str, int]] = None


class CommingMessage(BaseModel):
    """
    外来消息
    """
    # 用户ID
    userid: Optional[Union[str, int]] = None
    # 用户名称
    username: Optional[str] = None
    # 消息渠道
    channel: Optional[MessageChannel] = None
    # 消息体
    text: Optional[str] = None


class NotificationSwitch(BaseModel):
    """
    消息开关
    """
    # 消息类型
    mtype: Optional[str] = None
    # 微信开关
    wechat: Optional[bool] = False
    # TG开关
    telegram: Optional[bool] = False
    # Slack开关
    slack: Optional[bool] = False
