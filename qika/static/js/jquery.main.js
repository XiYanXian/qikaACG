$(document).ready(function() {
	"use strict";

	jQuery('.dropdown-submenu > a').on("click", function(e){
	    jQuery(this).next('.dropdown-menu').parent('li').toggleClass('show');
	    jQuery(this).next('.dropdown-menu').toggleClass('show');
	    e.stopPropagation();
	    e.preventDefault();
	});

	initAddClass();
	// Add Class  init
	function initAddClass() {
		"use strict";
		
		jQuery('.pre-opener').on( "click", function(e){
			e.preventDefault();
			jQuery("body").toggleClass("pre-active");
		});
	}

	initSlickCarousel();
	// slick init
	function initSlickCarousel() {
		jQuery('.bannerSlider').slick({
			slidesToScroll: 1,
			rows: 0,
			prevArrow: '<a href="#" class="slickPrev ti-angle-left d-flex align-items-center justify-content-center"><span class="sr-only">Previous slide</span></a>',
			nextArrow: '<a href="#" class="slickNext ti-angle-right d-flex align-items-center justify-content-center"><span class="sr-only">Next slide</span></a>',
			autoplay: true,
			autoplaySpeed: 10000,
			speed: 2000,
			fade: true,
			dots: false,
			adaptiveHeight: true,
			pauseOnHover: false,
			responsive: [{
				breakpoint: 768,
				settings: {
					arrows: false,
					dots: true,
					dotsClass: 'slickDots d-flex justify-content-center flex-wrap list-unstyled'
				}
			}]
		});

		jQuery('.testimonialSingleSlider').slick({
			slidesToScroll: 1,
			rows: 0,
			arrows: false,
			fade: true,
			infinite: false,
			adaptiveHeight: true,
			asNavFor: '.testimonialSwitcherSlider',
			responsive: [{
				breakpoint: 768,
				settings: {
					fade: false
				}
			}]
		});

		jQuery('.testimonialSwitcherSlider').slick({
			slidesToScroll: 1,
			slidesToShow: 3,
			rows: 0,
			prevArrow: '<a href="#" class="slickPrev ei_arrow_left d-flex align-items-center justify-content-center"><span class="sr-only">Previous slide</span></a>',
			nextArrow: '<a href="#" class="slickNext ei_arrow_right d-flex align-items-center justify-content-center"><span class="sr-only">Next slide</span></a>',
			infinite: false,
			variableWidth: true,
			asNavFor: '.testimonialSingleSlider',
			focusOnSelect: true
		});

		jQuery('.testimonialSingleSlider02').slick({
			slidesToScroll: 1,
			rows: 0,
			arrows: false,
			adaptiveHeight: true,
			asNavFor: '.testimonialSwitcherSlider02'
		});

		jQuery('.testimonialSwitcherSlider02').slick({
			slidesToScroll: 1,
			slidesToShow: 3,
			rows: 0,
			prevArrow: '<a href="#" class="slickPrev ei_arrow_left d-flex align-items-center justify-content-center"><span class="sr-only">Previous slide</span></a>',
			nextArrow: '<a href="#" class="slickNext ei_arrow_right d-flex align-items-center justify-content-center"><span class="sr-only">Next slide</span></a>',
			variableWidth: true,
			asNavFor: '.testimonialSingleSlider02',
			focusOnSelect: true,
			centerMode: true,
			centerPadding: '30px'
		});

		jQuery('.bannerSlider03').slick({
			slidesToScroll: 1,
			rows: 0,
			fade: true,
			prevArrow: '<a href="#" class="slickPrev ti-angle-left d-flex align-items-center justify-content-center"><span class="sr-only">Previous slide</span></a>',
			nextArrow: '<a href="#" class="slickNext ti-angle-right d-flex align-items-center justify-content-center"><span class="sr-only">Next slide</span></a>',
			adaptiveHeight: true,
			asNavFor: '.bsSwitcher03',
			responsive: [{
				breakpoint: 1440,
				settings: {
					arrows: false
				}
			}]
		});

		jQuery('.bsSwitcher03').slick({
			slidesToScroll: 1,
			slidesToShow: 4,
			rows: 0,
			arrows: false,
			dots: false,
			asNavFor: '.bannerSlider03',
			focusOnSelect: true,
			responsive: [{
				breakpoint: 768,
				settings: {
					slidesToShow: 1,
					centerMode: true,
					centerPadding: '0px'
				}
			}]
		});

		jQuery('.prjctCatagoriesSlider').slick({
			slidesToScroll: 1,
			rows: 0,
			arrows: false,
			fade: true,
			adaptiveHeight: true,
			asNavFor: '.prjctSwitcherSlider',
		});

		jQuery('.prjctSwitcherSlider').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 8,
			arrows: false,
			asNavFor: '.prjctCatagoriesSlider',
			focusOnSelect: true,
			variableWidth: true,
			responsive: [{
				breakpoint: 992,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 5,
					centerMode: true,
					centerPadding: '0px'
				}
			}, {
				breakpoint: 576,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 2,
					centerMode: true,
					centerPadding: '0px'
				}
			}]
		});

		jQuery('.prPostsSlider').slick({
			slidesToScroll: 2,
			rows: 0,
			slidesToShow: 5,
			arrows: false,
			dots: true,
			dotsClass: 'slickBars d-flex justify-content-center flex-wrap list-unstyled',
			adaptiveHeight: true,
			responsive: [{
				breakpoint: 1440,
				settings: {
					slidesToScroll: 2,
					slidesToShow: 4
				}
			}, {
				breakpoint: 1230,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 3
				}
			}, {
				breakpoint: 768,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 2
				}
			}, {
				breakpoint: 576,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 1
				}
			}]
		});

		jQuery('.swwdColumnsSlider').slick({
			slidesToScroll: 2,
			rows: 0,
			slidesToShow: 3,
			arrows: false,
			dots: true,
			dotsClass: 'slickBars d-flex justify-content-center flex-wrap list-unstyled',
			adaptiveHeight: true,
			responsive: [{
				breakpoint: 992,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 2
				}
			}, {
				breakpoint: 768,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 1
				}
			}]
		});

		jQuery('.swwdColumnsSliderType2').slick({
			slidesToScroll: 2,
			rows: 0,
			slidesToShow: 3,
			arrows: true,
			prevArrow: '<a href="#" class="slickPrev ti-angle-left d-flex align-items-center justify-content-center"><span class="sr-only">Previous slide</span></a>',
			nextArrow: '<a href="#" class="slickNext ti-angle-right d-flex align-items-center justify-content-center"><span class="sr-only">Next slide</span></a>',
			adaptiveHeight: true,
			responsive: [{
				breakpoint: 1500,
				settings: {
					arrows: false,
					dots: true,
					dotsClass: 'slickBars d-flex justify-content-center flex-wrap list-unstyled'
				}
			}, {
				breakpoint: 992,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 2,
					arrows: false,
					dots: true,
					dotsClass: 'slickBars d-flex justify-content-center flex-wrap list-unstyled'
				}
			}, {
				breakpoint: 768,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 1,
					arrows: false,
					dots: true,
					dotsClass: 'slickBars d-flex justify-content-center flex-wrap list-unstyled'
				}
			}]
		});

		jQuery('.npProjectsSlider').slick({
			slidesToScroll: 1,
			rows: 0,
			prevArrow: '<a href="#" class="slickPrev ei_arrow_left"><span class="sr-only">Previous slide</span></a>',
			nextArrow: '<a href="#" class="slickNext ei_arrow_right"><span class="sr-only">Next slide</span></a>',
			adaptiveHeight: true,
			responsive: [{
				breakpoint: 576,
				settings: {
					arrows: false
				}
			}]
		});

		jQuery('.blpPostsSlider').slick({
			slidesToScroll: 2,
			slidesToShow: 3,
			rows: 0,
			arrows: false,
			dots: true,
			dotsClass: 'slickDots d-flex justify-content-center flex-wrap list-unstyled',
			adaptiveHeight: true,
			responsive: [{
				breakpoint: 992,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 2
				}
			}, {
				breakpoint: 768,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 1
				}
			}]
		});

		jQuery('.detailsImageSlider').slick({
			slidesToScroll: 1,
			rows: 0,
			arrows: false,
			fade: true,
			adaptiveHeight: true,
			asNavFor: '.disSwitcherSlider'
		});

		jQuery('.disSwitcherSlider').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 4,
			arrows: false,
			adaptiveHeight: true,
			asNavFor: '.detailsImageSlider',
			focusOnSelect: true,
			responsive: [{
				breakpoint: 1230,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 3,
					centerMode: true,
					centerPadding: '0px'
				}
			}, {
				breakpoint: 576,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 2,
					centerMode: true,
					centerPadding: '0px'
				}
			}]
		});

		jQuery('.prjctDetaiIImageSlider').slick({
			slidesToScroll: 1,
			rows: 0,
			arrows: false,
			fade: true,
			asNavFor: '.prjctDtSliderSwitcher'
		});

		jQuery('.prjctDtSliderSwitcher').slick({
			slidesToScroll: 1,
			rows: 0,
			slidesToShow: 4,
			arrows: false,
			vertical: true,
			asNavFor: '.prjctDetaiIImageSlider',
			focusOnSelect: true,
			responsive: [{
				breakpoint: 992,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 3
				}
			}, {
				breakpoint: 576,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 3,
					vertical: false,
					centerMode: true,
					centerPadding: '0px'
				}
			}]
		});

		jQuery('.rpPosterSlider').slick({
			slidesToScroll: 1,
			slidesToShow: 2,
			rows: 0,
			prevArrow: '<a href="#" class="slickPrev ti-angle-left d-flex align-items-center justify-content-center"><span class="sr-only">Previous slide</span></a>',
			nextArrow: '<a href="#" class="slickNext ti-angle-right d-flex align-items-center justify-content-center"><span class="sr-only">Next slide</span></a>',
			responsive: [{
				breakpoint: 1230,
				settings: {
					slidesToScroll: 1,
					slidesToShow: 1
				}
			}]
		});

		jQuery('.feature-sec').slick({
		    dots: false,
		    speed: 800,
		    infinite: true,
		    slidesToShow: 5,
		    slidesToScroll: 1,
		    adaptiveHeight: true,
		    autoplay: true,
		    arrows: false,
		    autoplaySpeed: 4000,
		    responsive: [
		        {
		        breakpoint: 1199,
			        settings: {
			            slidesToShow: 3,
			            slidesToScroll: 3,
			        }
		        },
		        {
		        breakpoint: 1023,
			        settings: {
			            slidesToShow: 2,
			            slidesToScroll: 1,
			        }
		        },
		        {
		        breakpoint: 767,
			        settings: {
			            slidesToShow: 1,
			            slidesToScroll: 1,
			        }
		        }
		    ]
		});
	}

	initHasHover();
	// add classes on hover/touch
	function initHasHover() {
		jQuery('.hasOver').touchHover({});
	}

	initFancybox();
	// lightbox init
	function initFancybox() {
		jQuery('a.lightbox, [data-fancybox]').fancybox({
			parentEl: 'body',
			margin: [50, 0],
			gutter: 0,
			slideShow: false
		});
	}

	initInViewport();
	// in view port init
	function initInViewport() {
		jQuery('.hasViewport').itemInViewport({
			activeClass: 'inViewport',
			//once: true,
			visibleMode: 2 // 1 - full block, 2 - half block, 3 - immediate, 4... - custom
		});

		jQuery('.hasViewport__3').itemInViewport({
			activeClass: 'inViewport',
			//once: true,
			visibleMode: 3 // 1 - full block, 2 - half block, 3 - immediate, 4... - custom
		});
	}

	initStickyScrollBlock();
	// initialize fixed blocks on scroll
	function initStickyScrollBlock() {
		ResponsiveHelper.addRange({
			'767..': {
				on: function() {
					jQuery('.headerFixer').stickyScrollBlock({
						setBoxHeight: true,
						activeClass: 'fixedPosition',
						positionType: 'fixed',
						extraTop: function() {
							var totalHeight = 0;
							jQuery('0').each(function() {
								totalHeight += jQuery(this).outerHeight();
							});
							return totalHeight;
						}
					});
				},
				off: function() {
					jQuery('.headerFixer').stickyScrollBlock('destroy');
				}
			}
		});
	}


	initPreLoader()
	// PreLoader init
	function initPreLoader() {
	    "use strict";

	    jQuery('#loader').delay(1000).fadeOut();
	}
	
	initbackTop();
	// backtop init
	function initbackTop() {
		"use strict";

	    var jQuerybackToTop = jQuery("#back-top");
	    jQuery(window).on('scroll', function() {
	        if (jQuery(this).scrollTop() > 100) {
	            jQuerybackToTop.addClass('active');
	        } else {
	            jQuerybackToTop.removeClass('active');
	        }
	    });
	    jQuerybackToTop.on('click', function(e) {
	        jQuery("html, body").animate({scrollTop: 0}, 900);
	    });
	}

	initCounter();
	// Counter init
	function initCounter() {
		"use strict";

		jQuery('.counter').counterUp({
			delay: 10,
			time: 2000
		});
	}
	
});

jQuery(window).on('load', function() {

	"use strict";


	initIsoTop();
	// IsoTop init
	function initIsoTop() {
		"use strict";

		var isotopeHolder = jQuery('.isoContentHolder'),
			win = jQuery(window);
		jQuery('.isoFiltersList a').on( "click", function(e){
			e.preventDefault();
			
			jQuery('.isoFiltersList li').removeClass('active');
			jQuery(this).parent('li').addClass('active');
			var selector = jQuery(this).attr('data-filter');
			isotopeHolder.isotope({ filter: selector });
		});
		jQuery('.isoContentHolder').isotope({
			itemSelector: '.isoCol',
			transitionDuration: '0.6s',
			masonry: {
				columnWidth: '.isoCol'
			}
		});
	}
});