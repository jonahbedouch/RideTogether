import type { PageLoad } from './$types';
 
export const load: PageLoad = (async ({ fetch, params }) => {
  const res = await fetch(`http://127.0.0.1:8000/stupid`, {method: 'POST'});
  const item = await res.json();
 
  return { item };
})