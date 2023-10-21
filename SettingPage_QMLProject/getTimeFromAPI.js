function getTimeFromAPI() {
  const response = fetch("https://timeapi.io/api/Time/current/zone?timeZone=Asia/Tehran");

  if (response.ok) {
    const data = await(response.json())

    const hour = data.hour;
    const minute = data.minute;

    return { hour, minute };
  } else {
    throw new Error("خطا در دریافت پاسخ از API");
  }
}
