/*
 * generate by tool
*/
//using System.Collections;
//using System.Collections.Generic;
//using System.Linq;
//using LitJson;
//using FixedPointy;
namespace Table
{
    
    
    
       
    public class ResourceConfig : BaseTable
    {
        
        /// <summary>
        ///ID
        /// </summary>
        public int id; 
        
        /// <summary>
        ///资源名称
        /// </summary>
        public string name; 
        
        /// <summary>
        ///资源路径
        /// </summary>
        public string path; 
        
        /// <summary>
        ///后缀
        /// </summary>
        public string ext; 
        
        /// <summary>
        ///资源类型
        /// </summary>
        public int type; 
        
        /// <summary>
        ///资源标签
        /// </summary>
        public string tag; 
        

        
        public int Id { get => id; }     
        
        public string Name { get => name; }     
        
        public string Path { get => path; }     
        
        public string Ext { get => ext; }     
        
        public int Type { get => type; }     
        
        public string Tag { get => tag; }     
        

    } 
}