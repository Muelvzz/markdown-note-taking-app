export function formatDateTime(isoString: string): string {
  const date = new Date(isoString);

  if (isNaN(date.getTime())) {
    throw new Error("Invalid date string provided.");
  }

  const formatter = new Intl.DateTimeFormat('en-US', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
    hour12: true
  });

  return formatter.format(date);
}