class LSMTreeCompactor:
    """LSM-Tree SSTable Multi-Way Leveled Compaction Engine."""
    def compact(self, sstables: list[list[tuple[str, str]]]) -> list[tuple[str, str]]:
        # Merges list of sorted SSTables where later tables have higher timestamp/priority
        combined = {}
        for sst in sstables:
            for k, v in sst:
                combined[k] = v # Overwrite with newer versions / tombstones

        # Return sorted by key, filtering out tombstones ("__DELETED__")
        compacted = sorted([(k, v) for k, v in combined.items() if v != "__DELETED__"], key=lambda x: x[0])
        return compacted
