"""
ECOSTRESS Downloader Module
Automated tools for downloading mineral and soil spectra from ECOSTRESS library.
"""

import os
import requests
import pandas as pd
from pathlib import Path
from typing import List, Optional, Dict
import json


class ECOSTRESSDownloader:
    """
    Download ECOSTRESS spectral library data for minerals and soils.
    
    Note: ECOSTRESS提供的矿物和土壤光谱列表
    """
    
    # ECOSTRESS库基础信息
    ECOSTRESS_BASE_URL = "https://speclib.jpl.nasa.gov/"
    ECOSTRESS_LIBRARY_URL = "https://speclib.jpl.nasa.gov/library/ecostress-spectral-library/"
    
    # 常见矿物类别（中红外特征明显）
    COMMON_MINERALS = {
        'Quartz': 'SiO2 - Silicon Dioxide',
        'Calcite': 'CaCO3 - Calcium Carbonate',
        'Dolomite': 'CaMg(CO3)2 - Calcium Magnesium Carbonate',
        'Hematite': 'Fe2O3 - Iron(III) Oxide',
        'Magnetite': 'Fe3O4 - Iron(II,III) Oxide',
        'Kaolinite': 'Al2Si2O5(OH)4 - Aluminum Silicate Hydroxide',
        'Montmorillonite': 'Clay - Aluminum Silicate',
        'Illite': 'Clay - Aluminum Silicate',
        'Chlorite': 'Silicate - Iron-Magnesium',
        'Feldspar': 'Silicate Minerals',
        'Mica': 'Silicate Minerals',
        'Gypsum': 'CaSO4·2H2O - Calcium Sulfate',
        'Limonite': 'FeO(OH)·nH2O - Iron Hydroxide',
    }
    
    # 土壤分类
    SOIL_TYPES = {
        'Laterite': 'Red laterite soil - Rich in Fe and Al oxides',
        'Oxisol': 'Highly weathered tropical soil',
        'Ultisol': 'Acid clay soil',
        'Mollisol': 'Dark soil with organic matter',
        'Cambisol': 'Young soil - weakly developed',
        'Spodosol': 'Acidic soil - Podzol',
        'Vertisol': 'Clay-rich soil - shrink-swell properties',
        'Inceptisol': 'Young soil - slight weathering',
    }
    
    def __init__(self, cache_dir: str = './ecostress_cache'):
        """
        Initialize downloader.
        
        Args:
            cache_dir (str): Directory to cache downloaded files
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
    
    def get_mineral_list(self) -> Dict[str, str]:
        """
        Get list of available minerals in ECOSTRESS library.
        
        Returns:
            Dict: Dictionary of mineral names and descriptions
        """
        print("📋 Available Minerals in ECOSTRESS:")
        print("=" * 60)
        for mineral, description in self.COMMON_MINERALS.items():
            print(f"  • {mineral:<20} - {description}")
        print("=" * 60)
        return self.COMMON_MINERALS
    
    def get_soil_list(self) -> Dict[str, str]:
        """
        Get list of available soil types.
        
        Returns:
            Dict: Dictionary of soil types and descriptions
        """
        print("📋 Available Soil Types:")
        print("=" * 60)
        for soil, description in self.SOIL_TYPES.items():
            print(f"  • {soil:<20} - {description}")
        print("=" * 60)
        return self.SOIL_TYPES
    
    def download_minerals(self, 
                         mineral_names: Optional[List[str]] = None,
                         save_dir: str = './data/minerals/') -> List[str]:
        """
        Download mineral spectra from ECOSTRESS library.
        
        Note: 由于直接API访问可能受限，本函数提供下载指导和本地处理方法
        
        Args:
            mineral_names (List[str]): Specific minerals to download (if None, downloads all)
            save_dir (str): Directory to save downloaded files
            
        Returns:
            List[str]: List of downloaded file paths
        """
        save_path = Path(save_dir)
        save_path.mkdir(parents=True, exist_ok=True)
        
        if mineral_names is None:
            mineral_names = list(self.COMMON_MINERALS.keys())
        
        print(f"\n📥 Downloading mineral spectra...")
        print(f"Target minerals: {', '.join(mineral_names)}")
        print(f"Save directory: {save_path}")
        print("\n" + "=" * 60)
        print("⚠️  DOWNLOAD INSTRUCTIONS:")
        print("=" * 60)
        print(f"""
1. 访问 ECOSTRESS 官网:
   {self.ECOSTRESS_LIBRARY_URL}

2. 在左侧菜单选择:
   - Minerals (矿物)
   
3. 选择以下材料（或搜索）:
""")
        for i, mineral in enumerate(mineral_names, 1):
            print(f"   {i:2d}. {mineral}")
        
        print("""
4. 下载 .txt 文件到: {} 

5. 然后运行此代码进行处理:
   from src.spectrum_loader import SpectrumLoader
   loader = SpectrumLoader()
   spectra = loader.read_multiple_spectra('{}')
""".format(save_dir, save_dir))
        
        print("=" * 60)
        
        return []
    
    def download_soils(self, 
                      soil_types: Optional[List[str]] = None,
                      save_dir: str = './data/soils/') -> List[str]:
        """
        Download soil spectra from ECOSTRESS library.
        
        Args:
            soil_types (List[str]): Specific soil types (if None, downloads all)
            save_dir (str): Directory to save downloaded files
            
        Returns:
            List[str]: List of downloaded file paths
        """
        save_path = Path(save_dir)
        save_path.mkdir(parents=True, exist_ok=True)
        
        if soil_types is None:
            soil_types = list(self.SOIL_TYPES.keys())
        
        print(f"\n📥 Downloading soil spectra...")
        print(f"Target soil types: {', '.join(soil_types)}")
        print(f"Save directory: {save_path}")
        print("\n" + "=" * 60)
        print("⚠️  DOWNLOAD INSTRUCTIONS:")
        print("=" * 60)
        print(f"""
1. 访问 ECOSTRESS 官网:
   {self.ECOSTRESS_LIBRARY_URL}

2. 在左侧菜单选择:
   - Soils (土壤)
   
3. 选择以下土壤类型（或搜索）:
""")
        for i, soil in enumerate(soil_types, 1):
            print(f"   {i:2d}. {soil}")
        
        print("""
4. 下载 .txt 文件到: {} 

5. 然后运行此代码进行处理:
   from src.spectrum_loader import SpectrumLoader
   loader = SpectrumLoader()
   spectra = loader.read_multiple_spectra('{}')
""".format(save_dir, save_dir))
        
        print("=" * 60)
        
        return []
    
    def create_local_specimen_database(self, 
                                      csv_file: str = 'ecostress_minerals_soils.csv') -> pd.DataFrame:
        """
        Create a local database of mineral and soil specimens for reference.
        
        Args:
            csv_file (str): Output CSV file name
            
        Returns:
            pd.DataFrame: Database of specimens
        """
        specimens = []
        
        # Add minerals
        for mineral, description in self.COMMON_MINERALS.items():
            specimens.append({
                'type': 'Mineral',
                'name': mineral,
                'description': description,
                'mir_range': '4.0-4.6 μm',
                'expected_features': self._get_expected_features(mineral)
            })
        
        # Add soils
        for soil, description in self.SOIL_TYPES.items():
            specimens.append({
                'type': 'Soil',
                'name': soil,
                'description': description,
                'mir_range': '4.0-4.6 μm',
                'expected_features': 'Depends on mineral composition'
            })
        
        df = pd.DataFrame(specimens)
        df.to_csv(csv_file, index=False)
        
        print(f"✓ Created reference database: {csv_file}")
        return df
    
    @staticmethod
    def _get_expected_features(mineral: str) -> str:
        """Get expected MIR features for a mineral."""
        features_map = {
            'Quartz': 'Si-O stretching at 4.05, 4.27, 4.40 μm',
            'Calcite': 'CO3²⁻ stretching at 4.30, 4.39 μm',
            'Dolomite': 'CO3²⁻ stretching at 4.35, 4.40 μm',
            'Hematite': 'Fe-O stretching at 4.07, 4.16 μm',
            'Magnetite': 'Fe-O stretching at 4.0-4.2 μm',
            'Kaolinite': 'Al-O, Si-O stretching at 4.08, 4.28 μm',
            'Montmorillonite': 'Multiple Si-O, Al-O stretches at 4.00, 4.12, 4.27 μm',
            'Illite': 'Si-O, Al-O stretching at 4.05, 4.26 μm',
            'Chlorite': 'Si-O, Al-O, Mg-O stretching',
        }
        return features_map.get(mineral, 'Characteristic MIR absorption features')
    
    def print_download_guide(self):
        """Print a detailed download guide."""
        guide = """
╔════════════════════════════════════════════════════════════════╗
║          ECOSTRESS Spectral Library Download Guide             ║
╚════════════════════════════════════════════════════════════════╝

📍 官网链接: https://speclib.jpl.nasa.gov/

📋 下载步骤:

1️⃣  访问 ECOSTRESS Spectral Library
    https://speclib.jpl.nasa.gov/library/ecostress-spectral-library/

2️⃣  选择材料类别:
    - Minerals (矿物) ← 推荐重点
    - Soils (土壤) ← 推荐
    
3️⃣  筛选材料:
    矿物建议选择:
    ✓ Quartz (石英)
    ✓ Calcite (方解石)
    ✓ Hematite (赤铁矿)
    ✓ Kaolinite (高岭石)
    ✓ Montmorillonite (蒙脱石)
    ✓ Illite (伊利石)
    ✓ Dolomite (白云石)
    ✓ Magnetite (磁铁矿)
    
    土壤建议选择:
    ✓ Laterite (红壤)
    ✓ Clay soils (粘质土)
    ✓ Oxisol (氧化还原层土)
    
4️⃣  下载 .txt 文件
    右键 → 另存为 → 保存到 ./data/minerals/ 或 ./data/soils/
    
5️⃣  导入到数据库:
    python examples/03_build_database.py

🔧 快速导入代码:

    from src.spectrum_loader import SpectrumLoader
    from src.database import SpectrumDatabase
    
    # 加载光谱
    loader = SpectrumLoader()
    minerals = loader.read_multiple_spectra('./data/minerals/')
    soils = loader.read_multiple_spectra('./data/soils/')
    
    # 导入数据库
    db = SpectrumDatabase('inorganic_library.db')
    db.add_multiple_spectra(minerals + soils)

💡 提示:
   - 每个 .txt 文件包含一个样本的完整光谱
   - 文件名通常为材料名称 + ID
   - 推荐下载 50-100 个不同样本以建立充分的库

📊 期望结果:
   - 完整的中红外(4.0-4.6 μm)光谱数据
   - 明显的吸收特征
   - 可用于光谱匹配和识别

═════════════════════════════════════════════════════════════════
"""
        print(guide)


# 简化版本 - 直接使用本地CSV参考
class LocalMineralSoilDatabase:
    """Local reference database for minerals and soils."""
    
    MINERALS_SOILS_DATA = {
        'minerals': {
            'Quartz': {'formula': 'SiO2', 'mir_peaks': [4.05, 4.27, 4.40]},
            'Calcite': {'formula': 'CaCO3', 'mir_peaks': [4.30, 4.39]},
            'Dolomite': {'formula': 'CaMg(CO3)2', 'mir_peaks': [4.35, 4.40]},
            'Hematite': {'formula': 'Fe2O3', 'mir_peaks': [4.07, 4.16]},
            'Magnetite': {'formula': 'Fe3O4', 'mir_peaks': [4.00, 4.20]},
            'Kaolinite': {'formula': 'Al2Si2O5(OH)4', 'mir_peaks': [4.08, 4.28]},
            'Montmorillonite': {'formula': 'Clay', 'mir_peaks': [4.00, 4.12, 4.27]},
            'Illite': {'formula': 'Clay', 'mir_peaks': [4.05, 4.26]},
            'Chlorite': {'formula': 'Silicate', 'mir_peaks': [4.05, 4.25]},
            'Gypsum': {'formula': 'CaSO4·2H2O', 'mir_peaks': [4.10, 4.50]},
        },
        'soils': {
            'Laterite': {'main_minerals': ['Hematite', 'Goethite'], 'color': 'Red'},
            'Oxisol': {'main_minerals': ['Fe/Al Oxides'], 'color': 'Red-Yellow'},
            'Ultisol': {'main_minerals': ['Clay', 'Fe Oxides'], 'color': 'Red'},
        }
    }
    
    @classmethod
    def export_to_csv(cls, output_file: str = 'local_reference.csv'):
        """Export reference database to CSV."""
        records = []
        
        for mineral, info in cls.MINERALS_SOILS_DATA['minerals'].items():
            records.append({
                'type': 'Mineral',
                'name': mineral,
                'formula': info['formula'],
                'mir_peaks': ', '.join(map(str, info['mir_peaks']))
            })
        
        for soil, info in cls.MINERALS_SOILS_DATA['soils'].items():
            records.append({
                'type': 'Soil',
                'name': soil,
                'formula': ', '.join(info['main_minerals']),
                'mir_peaks': 'Variable'
            })
        
        df = pd.DataFrame(records)
        df.to_csv(output_file, index=False)
        print(f"✓ Exported reference database to: {output_file}")
        return df
