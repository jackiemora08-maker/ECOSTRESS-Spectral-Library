# ECOSTRESS Inorganic Spectral Library Database

专注于**矿物和土壤**的光谱库数据库，用于中红外（MIR, 4.0-4.6 μm）光谱分析。

## 🎯 项目目标

- 📊 从ECOSTRESS库中筛选矿物和土壤样本
- 🔬 重点关注中红外（4.0-4.6 μm）区间的宽带特征
- 💾 建立SQLite光谱数据库
- 📈 光谱分析和指纹识别
- 🎨 中红外特征可视化

## 💎 涵盖的无机物材料

### 矿物类 (Minerals)
- 石英（Quartz）- SiO₂
- 长石（Feldspars）
- 方解石（Calcite）- CaCO₃
- 白云石（Dolomite）- CaMg(CO₃)₂
- 赤铁矿（Hematite）- Fe₂O₃
- 磁铁矿（Magnetite）- Fe₃O₄
- 云母（Micas）
- 绿泥石（Chlorite）
- 高岭石（Kaolinite）- Al₂Si₂O₅(OH)₄
- 蒙脱石（Montmorillonite）
- 伊利石（Illite）

### 土壤类 (Soils)
- 红壤（Laterite/Oxisol）
- 黄壤（Ultisol）
- 褐壤（Cambisol）
- 黑壤（Mollisol）
- 灰壤（Spodosol）
- 盐碱土（Salic soil）
- 砾质土壤（Gravelly soils）
- 粘质土壤（Clay soils）

## 📋 中红外特征

中红外区间（4.0-4.6 μm, 2500-2173 cm⁻¹）的典型吸收特征：

| 材料 | 吸收峰 (μm) | 功能团 |
|------|------------|--------|
| 石英 | 4.0-4.2 | Si-O伸缩振动 |
| 方解石 | 4.3-4.5 | CO₃²⁻ C-O伸缩 |
| 高岭石 | 4.1-4.3 | Si-O, Al-O伸缩 |
| 蒙脱石 | 4.0-4.6 | 多种Si-O伸缩 |
| 赤铁矿 | 4.0-4.2 | Fe-O伸缩 |

## 🚀 快速开始

### 1. 安装依赖

```bash
git clone https://github.com/jackiemora08-maker/ECOSTRESS-Spectral-Library.git
cd ECOSTRESS-Spectral-Library
pip install -r requirements.txt
```

### 2. 下载矿物/土壤光谱

```python
from src.ecostress_downloader import ECOSTRESSDownloader

# 初始化下载器
downloader = ECOSTRESSDownloader()

# 下载矿物光谱
minerals = downloader.download_minerals(
    categories=['Quartz', 'Calcite', 'Hematite', 'Kaolinite', 'Montmorillonite'],
    save_dir='./data/minerals/'
)

# 下载土壤光谱
soils = downloader.download_soils(
    save_dir='./data/soils/'
)
```

### 3. 构建数据库

```python
from src.database import SpectrumDatabase
from src.spectrum_loader import SpectrumLoader

db = SpectrumDatabase('inorganic_library.db')
loader = SpectrumLoader()

# 批量导入矿物光谱
mineral_spectra = loader.read_multiple_spectra('./data/minerals/')
db.add_multiple_spectra(mineral_spectra)

# 批量导入土壤光谱
soil_spectra = loader.read_multiple_spectra('./data/soils/')
db.add_multiple_spectra(soil_spectra)
```

### 4. 中红外分析

```python
from src.mir_analyzer import MIRAnalyzer

analyzer = MIRAnalyzer()

# 提取中红外特征（4.0-4.6 μm）
spectrum = db.get_spectral_data(spectrum_id=1)
mir_features = analyzer.extract_mir_features(spectrum)

# 绘制中红外区间
analyzer.plot_mir_region(spectrum, save_path='mir_spectrum.png')

# 进行光谱匹配
match_result = analyzer.spectral_matching(
    unknown_spectrum=query_spectrum,
    library_db=db,
    method='mir_focus'  # 重点关注MIR区间
)
```

## 📁 项目结构

```
ECOSTRESS-Spectral-Library/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── spectrum_loader.py        # 光谱文件读取
│   ├── database.py               # SQLite数据库管理
│   ├── mir_analyzer.py           # 中红外分析工具（新）
│   ├── ecostress_downloader.py   # ECOSTRESS下载工具（新）
│   ├── spectrum_analysis.py      # 光谱分析工具
│   └── visualization.py          # 可视化模块
├── examples/
│   ├── 01_download_minerals.py           # 下载矿物光谱
│   ├── 02_download_soils.py              # 下载土壤光谱
│   ├── 03_build_database.py              # 构建数据库
│   ├── 04_mir_analysis.py                # 中红外分析
│   ├── 05_spectral_matching.py           # 光谱匹配
│   └── 06_mir_visualization.py           # MIR可视化
├── data/
│   ├── minerals/                 # 矿物光谱文件
│   ├── soils/                    # 土壤光谱文件
│   └── sample_spectra/
├── tests/
│   └── test_mir_analysis.py
└── docs/
    ├── guide.md
    └── mir_wavelength_reference.md
```

## 🔗 ECOSTRESS光谱库链接

- 🌐 **官网**: https://speclib.jpl.nasa.gov/
- 📥 **下载**: https://speclib.jpl.nasa.gov/library/ecostress-spectral-library/

## 📚 参考文献

- Baldridge, A. M., et al. (2009). "The ASTER Spectral Library version 2.0." Remote Sensing of Environment.
- Hunt, G. R., & Salisbury, J. W. (1976). "Midinfrared reflectance spectra of minerals." Remote Sensing of Environment.

## 📝 License

MIT License
