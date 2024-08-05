function columnChart() {
  const columnChart = document.getElementById("column-chart");
  const dataIncome = parseChartData(columnChart, "data-chart-income");
  const dataExpense = parseChartData(columnChart, "data-chart-expense");

  const columnChartOptions = {
    colors: ["#31C48D", "#F05252"],
    series: [
      {
        name: "Thu nhập",
        color: "#31C48D",
        data: dataIncome,
      },
      {
        name: "Chi tiêu",
        color: "#F05252",
        data: dataExpense,
      },
    ],
    chart: {
      type: "bar",
      height: "320px",
      fontFamily: "Inter, sans-serif",
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "70%",
        borderRadiusApplication: "end",
        borderRadius: 8,
      },
    },
    tooltip: {
      shared: true,
      intersect: false,
      style: {
        fontFamily: "Inter, sans-serif",
      },
      theme: "dark",
      y: {
        formatter: function (val) {
          var Formatter = new Intl.NumberFormat("vi-VN", {
            style: "currency",
            currency: "VND",
          });

          return Formatter.format(val);
        },
      },
    },
    states: {
      hover: {
        filter: {
          type: "darken",
          value: 1,
        },
      },
    },
    stroke: {
      show: true,
      width: 0,
      colors: ["transparent"],
    },
    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: -14,
      },
    },
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
    },
    xaxis: {
      floating: false,
      labels: {
        show: true,
        style: {
          fontFamily: "Inter, sans-serif",
          cssClass: "text-xs font-normal fill-gray-500 dark:fill-gray-400",
        },
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
    },
    yaxis: {
      show: false,
    },
    fill: {
      opacity: 1,
    },
  };

  if (columnChart && typeof ApexCharts !== "undefined") {
    const chart = new ApexCharts(
      document.getElementById("column-chart"),
      columnChartOptions
    );
    chart.render();
  }
}

function parseChartData(el, attr) {
  const dataString = el.getAttribute(attr);
  return dataString.split("},").map((item) => {
    const [xPart, yPart] = item
      .replace(/[{}]/g, "")
      .trim()
      .split(",")
      .map((part) => part.split(":"));
    return {
      x: xPart[1].trim().replace(/'/g, ""),
      y: parseInt(yPart[1].trim()),
    };
  });
}

function formatNumber(value) {
  if (value >= 1_000_000_000) {
    return (value / 1_000_000_000).toFixed(1) + "tỷ";
  } else if (value >= 1_000_000) {
    return (value / 1_000_000).toFixed(1) + "tr";
  } else if (value >= 1_000) {
    return (value / 1_000).toFixed(0) + "k";
  } else {
    return value.toString();
  }
}

function donutChart(id) {
  const donutChart = document.getElementById(id);
  const labels = stringToArray(donutChart, "data-chart-label");
  const values = stringToArray(donutChart, "data-chart-value");

  const options = {
    series: values,
    colors: [
      "#1C64F2",
      "#16BDCA",
      "#FDBA8C",
      "#E74694",
      "#00D9DC",
      "#FC0000",
      "#00D700",
      "#00A2FF",
      "#FF9EAC",
    ],
    chart: {
      height: 320,
      width: "100%",
      type: "donut",
    },
    stroke: {
      colors: ["transparent"],
      lineCap: "",
    },
    plotOptions: {
      pie: {
        donut: {
          labels: {
            show: true,
            name: {
              show: true,
              fontFamily: "Inter, sans-serif",
              offsetY: 20,
            },
            total: {
              showAlways: true,
              show: true,
              label: "Tổng",
              fontFamily: "Inter, sans-serif",
              formatter: function (w) {
                const sum = w.globals.seriesTotals.reduce((a, b) => {
                  return a + b;
                }, 0);
                // return sum + "k";
                return formatNumber(sum);
              },
            },
            value: {
              show: true,
              fontFamily: "Inter, sans-serif",
              offsetY: -20,
              formatter: function (value) {
                return formatNumber(value);
              },
            },
          },
          size: "80%",
        },
      },
    },
    grid: {
      padding: {
        top: -2,
      },
    },
    labels: labels,
    dataLabels: {
      enabled: false,
    },
    legend: {
      position: "bottom",
      fontFamily: "Inter, sans-serif",
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return formatNumber(value);
        },
      },
    },
    xaxis: {
      labels: {
        formatter: function (value) {
          return formatNumber(value);
        },
      },
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
    },
  };

  if (document.getElementById(id) && typeof ApexCharts !== "undefined") {
    const chart = new ApexCharts(document.getElementById(id), options);
    chart.render();
  }
}

function stringToArray(el, attr) {
  const arrayString = el.getAttribute(attr);

  try {
    const jsonString = arrayString.replace(/'/g, '"');
    const array = JSON.parse(jsonString);

    if (Array.isArray(array)) {
      return array;
    } else {
      throw new Error("Parsed result is not an array");
    }
  } catch (e) {
    console.error("Invalid input string:", e);
    return [];
  }
}
