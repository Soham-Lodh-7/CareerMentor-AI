const form = document.getElementById('careerForm');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const data = {
    name: form.name.value,
    skills: form.skills.value,
    interests: form.interests.value,
    dream: form.dream.value
  };
  const response = await fetch('http://localhost:5000/recommend', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  const result = await response.json();
  alert(`Recommended Careers: ${result.careers.join(', ')}`);
});
