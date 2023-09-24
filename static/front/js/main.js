const product = new Swiper('#services-slider', {
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
    // spaceBetween : 10,
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
        slidesPerView:4,
      },
  
      // when window width is >= 640px
  
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
    // spaceBetween : 10,
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
        slidesPerView:4,
      },

      // when window width is >= 640px

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