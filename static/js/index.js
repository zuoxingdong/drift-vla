function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

window.addEventListener('scroll', () => {
  const scrollButton = document.querySelector('.scroll-to-top');
  if (!scrollButton) return;
  scrollButton.classList.toggle('visible', window.pageYOffset > 300);
});

function setupVideoAutoplay() {
  const videos = document.querySelectorAll('video[autoplay]');
  if (videos.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      const video = entry.target;
      if (entry.isIntersecting) {
        video.play().catch(() => {});
      } else {
        video.pause();
      }
    });
  }, { threshold: 0.5 });

  videos.forEach((video) => observer.observe(video));
}

document.addEventListener('DOMContentLoaded', setupVideoAutoplay);
