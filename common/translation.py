from modeltranslation.translator import translator, TranslationOptions
from common.models import News, NewsCategory, NewsTag,Region, Advertisement

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

class NewsTagTranslationOptions(TranslationOptions):
    fields = ('title',)

class RegionTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(News, NewsTranslationOptions)
translator.register(NewsCategory, NewsCategoryTranslationOptions)
translator.register(NewsTag, NewsTagTranslationOptions)
translator.register(Region, RegionTranslationOptions)
