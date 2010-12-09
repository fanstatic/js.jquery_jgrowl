from fanstatic import Library, ResourceInclusion

from js.jquery import jquery

library = Library('jquery_jgrowl', 'resources')

jquery_jgrowl_css = ResourceInclusion(library, 'jquery.jgrowl.css')

jquery_jgrowl = ResourceInclusion(library, 'jquery.jgrowl.js',
    minified='jquery.jgrowl_minimized.js',
    depends=[jquery, jquery_jgrowl_css])

