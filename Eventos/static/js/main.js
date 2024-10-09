const chart_limpieza = async () => {
  try {
    const response = await fetch(
      "http://127.0.0.1:8000/dashboard/reportes/chart_limpieza"
    );
    return await response.json();
  } catch (err) {
    alert(err);
  }
};

const chart_habitaciones = async () => {
  try {
    const response = await fetch(
      "http://127.0.0.1:8000/dashboard/reportes/chart_habitaciones"
    );
    return await response.json();
  } catch (err) {
    alert(err);
  }
};

const chart_stock = async () => {
  try {
    const response = await fetch(
      "http://127.0.0.1:8000/dashboard/reportes/chart_stock"
    );
    return await response.json();
  } catch (err) {
    alert(err);
  }
};

const initChart = async () => {
  const myChart = echarts.init(document.getElementById("chart"));
  const myChart1 = echarts.init(document.getElementById("chart1"));
  const myChart2 = echarts.init(document.getElementById("chart2"));
  const option = await chart_limpieza();
  const option1 = await chart_habitaciones();
  const option2 = await chart_stock();
  myChart.setOption(option);
  myChart1.setOption(option1);
  myChart2.setOption(option2);
  myChart.resize();
  myChart1.resize();
  myChart2.resize();
};

window.addEventListener("load", async () => {
  await initChart();
});
