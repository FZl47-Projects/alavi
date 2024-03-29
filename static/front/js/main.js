const product = new Swiper('.services-slider', {
    // Optional parameters
    direction: 'horizontal',
    grabCursor: true,
    allowSlideNext: true,
  
    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
      pauseOnMouseEnter: true,
    },
    slidesPerView: 3,
    spaceBetween : 20,

    breakpoints: {
      // when window width is >= 320px
      200: {
        slidesPerView: 1,
  
      },
      320: {
        slidesPerView: 1,
  
      },
      768: {
        slidesPerView: 2,
  
      },
      850: {
        slidesPerView: 2,
  
      },
      992: {
        slidesPerView: 3,
      },
      1600: {
        slidesPerView: 4,
      },
    },
    // If we need pagination
    // pagination: {
    //   el: '.swiper-pagination',
    //   clickable: true
    // },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });


const productsSwiper = new Swiper('#products-swiper', {
    // Optional parameters
    direction: 'horizontal',
    grabCursor: true,
    allowSlideNext: true,

    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
      pauseOnMouseEnter: true,
    },
    slidesPerView: 4,
    spaceBetween : 18,
    breakpoints: {
      200: {
        slidesPerView: 1,
      },
      320: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      850: {
        slidesPerView: 2,
        spaceBetween : 23,
      },
      992: {
        slidesPerView: 3,
        spaceBetween : 20,
      },
      1400: {
        slidesPerView: 4,
        spaceBetween : 18,
      },
    },
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
});


  const product2 = new Swiper('#certificate-slider', {
    // Optional parameters
    direction: 'horizontal',
    grabCursor: true,
    allowSlideNext: true,

    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
      pauseOnMouseEnter: true,
    },
    slidesPerView: 1,
    spaceBetween : 15,

    breakpoints: {
      // when window width is >= 320px
      200: {
        slidesPerView: 1,

      },
      320: {
        slidesPerView: 1,

      },
      768: {
        slidesPerView: 2,

      },
      850: {
        slidesPerView: 2,

      },
      992: {
        slidesPerView: 3,
      },
      1400: {
        slidesPerView: 4,
      },
    },
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });