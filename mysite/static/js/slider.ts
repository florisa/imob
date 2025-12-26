// slider.ts - TypeScript version for custom slider logic

document.addEventListener('DOMContentLoaded', () => {
  // down-payment slider logic
  const downPaymentSlider = document.getElementById('down-payment-slider') as HTMLInputElement | null;
  const downPaymentInput = document.getElementById('down-payment-input') as HTMLInputElement | null;
  const downPaymentRange = document.getElementById('down-payment-slider-range') as HTMLElement | null;
  const downPaymentThumbWrapper = document.getElementById('down-payment-slider-thumb-wrapper') as HTMLElement | null;
  const downPaymentThumb = document.getElementById('down-payment-slider-thumb') as HTMLElement | null;

  function updatedownPaymentSlider(val: number) {
    if (!downPaymentSlider || !downPaymentInput || !downPaymentRange || !downPaymentThumbWrapper || !downPaymentThumb) return;
    const min = parseInt(downPaymentSlider.min, 10);
    const max = parseInt(downPaymentSlider.max, 10);
    const percent = ((val - min) / (max - min)) * 100;
    downPaymentRange.style.left = '0%';
    downPaymentRange.style.right = (100 - percent) + '%';
    downPaymentThumbWrapper.style.left = `calc(${percent}% )`;
    downPaymentThumb.setAttribute('aria-valuenow', val.toString());
    downPaymentSlider.value = val.toString();
    downPaymentInput.value = val.toString();
  }

  if (downPaymentSlider && downPaymentInput) {
    downPaymentSlider.addEventListener('input', function () {
      updatedownPaymentSlider(Number((this as HTMLInputElement).value));
    });
    downPaymentInput.addEventListener('input', function () {
      let val = Math.max(parseInt(downPaymentInput.value, 10) || 0, parseInt(downPaymentSlider.min, 10));
      val = Math.min(val, parseInt(downPaymentSlider.max, 10));
      updatedownPaymentSlider(val);
    });
    updatedownPaymentSlider(Number(downPaymentSlider.value));
  }

  // Period slider logic
  const periodSlider = document.getElementById('period-slider') as HTMLInputElement | null;
  const periodRange = document.getElementById('period-slider-range') as HTMLElement | null;
  const periodThumbWrapper = document.getElementById('period-slider-thumb-wrapper') as HTMLElement | null;
  const periodThumb = document.getElementById('period-slider-thumb') as HTMLElement | null;
  const periodValueLabel = document.getElementById('period-value') as HTMLElement | null;

  function updateperiodSlider(val: number) {
    if (!periodSlider || !periodRange || !periodThumbWrapper || !periodThumb || !periodValueLabel) return;
    const min = parseInt(periodSlider.min, 10);
    const max = parseInt(periodSlider.max, 10);
    const percent = ((val - min) / (max - min)) * 100;
    periodRange.style.left = '0%';
    periodRange.style.right = (100 - percent) + '%';
    periodThumbWrapper.style.left = `calc(${percent}% )`;
    periodThumb.setAttribute('aria-valuenow', val.toString());
    periodSlider.value = val.toString();
    periodValueLabel.textContent = val.toString();
  }

  if (periodSlider) {
    periodSlider.addEventListener('input', function () {
      updateperiodSlider(Number((this as HTMLInputElement).value));
    });
    updateperiodSlider(Number(periodSlider.value));
  }
});

